---
layout: page
permalink: /publications/
title: publications
description: publications by categories in reversed chronological order.
years: [2023, 2020, 2019, 2018, 2016, 2013, 2011]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
