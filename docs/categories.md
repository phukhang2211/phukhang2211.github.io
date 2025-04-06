---
layout: page
title: Categories
permalink: /categories/
---

<div class="categories-container">
  <div class="categories-overview">
    {% for category in site.categories %}
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <a href="#{{ category_name | slugify }}" class="category-badge">
        {{ category_name | capitalize }} ({{ site.categories[category_name].size }})
      </a>
    {% endfor %}
  </div>

  <div class="categories-detail">
    {% for category in site.categories %}
      {% capture category_name %}{{ category | first }}{% endcapture %}
      <section class="category-section" id="{{ category_name | slugify }}">
        <h2 class="category-title">
          <span class="category-icon">📑</span>
          {{ category_name | capitalize }}
        </h2>
        <div class="post-list">
          {% for post in site.categories[category_name] %}
            <article class="post-item">
              <span class="post-date">{{ post.date | date: "%Y-%m-%-d" }}</span>
              <a href="{{ post.url | relative_url }}" class="post-link">{{ post.title }}</a>
            </article>
          {% endfor %}
        </div>
      </section>
    {% endfor %}
  </div>
</div>

<style>
.categories-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}

.categories-overview {
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #e9ecef;
  text-align: center;
}

.category-badge {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  margin: 0.25rem;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 15px;
  color: #495057;
  text-decoration: none;
  font-size: 0.9rem;
  transition: all 0.2s ease;
}

.category-badge:hover {
  background: #e9ecef;
  color: #1971c2;
}

.category-section {
  margin: 2rem 0;
  padding-top: 2rem;
  border-top: 1px solid #e9ecef;
}

.category-section:first-child {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}

.category-title {
  display: flex;
  align-items: center;
  font-size: 1.5rem;
  color: #343a40;
  margin-bottom: 1rem;
}

.category-icon {
  margin-right: 0.5rem;
}

.post-list {
  margin-left: 1rem;
}

.post-item {
  margin: 0.75rem 0;
  display: flex;
  align-items: baseline;
  gap: 1rem;
}

.post-date {
  color: #868e96;
  font-size: 0.9rem;
  white-space: nowrap;
}

.post-link {
  color: #495057;
  text-decoration: none;
  transition: color 0.2s ease;
}

.post-link:hover {
  color: #1971c2;
}

@media (max-width: 768px) {
  .categories-container {
    padding: 0.5rem;
  }
  
  .post-item {
    flex-direction: column;
    gap: 0.25rem;
  }
}
</style>