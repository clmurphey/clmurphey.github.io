# clmurphey.github.io

My academic website, built with [Hugo](https://gohugo.io/).

## Common updates

- **Add news:** copy a file in `content/news/`, then change the date and text.
- **Add a publication:** add it to `bibliography/publications.bib` with `keywords` set to `journal`, `conference`, `patent`, `other`, `talk`, or `poster`, then run `python3 scripts/bib_to_json.py`.
- **Update the CV:** replace `static/assets/pdf/CV_CLM.pdf`.
- **Edit the about page:** change `content/_index.md`.
- **Edit projects:** change `content/projects/`.

## Preview

Run `hugo server` and open http://localhost:1313.

## Publish

Push to `master`. GitHub builds the site and publishes it.
