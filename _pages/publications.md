---
layout: page
permalink: /publications/
title: publications
description: Publications by categories in reversed chronological order. 
years: [2023, 2020, 2019, 2018, 2016, 2013, 2011]
nav: true
nav_order: 3
---
<!-- _pages/publications.md -->
<div class="publications">
<p>For the most up-to-date publication information, please refer to my <a href="[../assets/pdf/CV_CLM.pdf](https://scholar.google.com/citations?user=HKWLUxAAAAAJ&hl=en)">Google Scholar Profile</a>.</p>
{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
