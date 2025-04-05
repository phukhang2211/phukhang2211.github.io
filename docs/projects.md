---
layout: page
title: Projects
permalink: /projects/
---

# Projects

{% for project in site.projects %}
  <div class="project">
    <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
    <p>{{ project.excerpt }}</p>
  </div>
{% endfor %}