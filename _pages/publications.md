---
layout: page
permalink: /publications/
title: publications
description: Publications by categories in reversed chronological order. 
years: [2024, 2023, 2020, 2019, 2018, 2016, 2013, 2011]
nav: true
nav_order: 3
---
<!-- _pages/publications.md -->
<div class="publications">
<p>For the most up-to-date publication information, please refer to my Google Scholar Profile.</p>
{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
