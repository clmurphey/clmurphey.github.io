---
layout: page
permalink: /publications/
title: publications
description:
nav: true
nav_order: 3
---
<!-- _pages/publications.md -->
<div class="publications">
<p>For presentations and the most up-to-date information, please refer to my <a href="{{ '/assets/pdf/CV_CLM.pdf' | relative_url }}">CV</a> or my <a href="https://scholar.google.com/citations?user=HKWLUxAAAAAJ">Google Scholar Profile</a>.</p>

<h2 class="year">journal articles</h2>
{% bibliography -f papers -q @*[keywords=journal]* %}

<h2 class="year">reviewed conference papers</h2>
{% bibliography -f papers -q @*[keywords=conference]* %}

<h2 class="year">patents</h2>
{% bibliography -f papers -q @*[keywords=patent]* %}

<h2 class="year">other publications</h2>
{% bibliography -f papers -q @*[keywords=other]* %}
</div>
