---
layout: page
title: Categories
permalink: /categories/
---

<div class="categories-page">
  {% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div class="category-section">
      <h2 id="{{ category_name }}">{{ category_name | capitalize }}</h2>
      <ul class="post-list">
        {% for post in site.categories[category_name] %}
          <li>
            <span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
            <h3>
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>
            {% if post.excerpt %}
              <p class="excerpt">{{ post.excerpt }}</p>
            {% endif %}
            {% if post.tags %}
              <div class="tags">
                {% for tag in post.tags %}
                  <span class="tag">{{ tag }}</span>
                {% endfor %}
              </div>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>

<style>
.post-list {
  list-style: none;
  padding-left: 0;
}
.post-meta {
  color: #666;
  font-size: 0.9em;
}
.excerpt {
  color: #666;
  font-size: 0.95em;
  margin: 5px 0;
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
.category-section {
  margin-bottom: 40px;
}
</style>