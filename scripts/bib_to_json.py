#!/usr/bin/env python3
# Turn bibliography/publications.bib into data/publications.json for Hugo.
# Run this after editing the .bib file: python3 scripts/bib_to_json.py
import json
import re

MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


# read one {...} value, keeping nested braces together
def braced(text, start):
    depth = 0
    for i in range(start, len(text)):
        depth += {"{": 1, "}": -1}.get(text[i], 0)
        if depth == 0:
            return text[start + 1:i], i + 1
    raise ValueError("unbalanced braces")


def parse(text):
    entries = []
    for match in re.finditer(r"@(\w+)\{([^,]+),", text):
        fields = {"type": match.group(1).lower(), "key": match.group(2)}
        pos = match.end()
        while True:
            field = re.compile(r"\s*(\w+)\s*=\s*").match(text, pos)
            if not field:
                break
            pos = field.end()
            if text[pos] == "{":
                value, pos = braced(text, pos)
            else:
                bare = re.compile(r"[^,\s}]+").match(text, pos)
                value, pos = bare.group(), bare.end()
            fields[field.group(1).lower()] = value.replace("{", "").replace("}", "").replace("--", "–").replace("'", "’")
            pos = re.compile(r"\s*,?").match(text, pos).end()
        entries.append(fields)
    return entries


def author(name):
    last, _, first = name.partition(", ")
    return {"first": first, "last": last}


def entry(fields):
    month = MONTHS.index(fields["month"]) + 1 if "month" in fields else 0
    venue = fields.get("journal", "")
    if "booktitle" in fields:
        venue = "In " + fields["booktitle"]
    date = fields["year"]
    if month:
        date = fields["month"].capitalize() + " " + date
    return {
        "key": fields["key"],
        "keyword": fields["keywords"],
        "title": fields["title"],
        "authors": [author(name) for name in fields["author"].split(" and ")],
        "venue": venue,
        "date": date,
        "note": fields.get("note", ""),
        "abstract": fields.get("abstract", ""),
        "html": fields.get("html", ""),
        "order": [int(fields["year"]), month],
    }


entries = [entry(f) for f in parse(open("bibliography/publications.bib", encoding="utf-8").read())]
entries.sort(key=lambda e: e["order"], reverse=True)
with open("data/publications.json", "w", encoding="utf-8") as out:
    json.dump(entries, out, ensure_ascii=False, indent=1)
print(len(entries), "entries written to data/publications.json")
