---
layout: page
title: Tutorials
permalink: /tutorials/
---

# Tutorials

## Markdown Tutorials
{% for post in site.categories.markdown %}
  <div class="tutorial">
    <h3>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    </h3>
    {% if post.excerpt %}
    <p>{{ post.excerpt }}</p>
    {% endif %}
    {% if post.tags %}
    <div class="tags">
      {% for tag in post.tags %}
        <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
{% endfor %}

## Beginner Tutorials
{% for post in site.categories.beginner %}
  <div class="tutorial">
    <h3>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
    </h3>
    {% if post.excerpt %}
    <p>{{ post.excerpt }}</p>
    {% endif %}
    {% if post.tags %}
    <div class="tags">
      {% for tag in post.tags %}
        <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
{% endfor %}

<style>
.tutorial {
  margin-bottom: 30px;
}
.post-date {
  color: #666;
  font-size: 0.8em;
  margin-left: 10px;
}
.tags {
  margin-top: 5px;
}
.tag {
  background: #f0f0f0;
  padding: 2px 8px;
  border-radius: 3px;
  font-size: 0.8em;
  margin-right: 5px;
}
</style>