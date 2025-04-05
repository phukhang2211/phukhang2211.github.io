<!-- ---
layout: post
title: "Complete Jekyll Objects and Variables Reference"
date:   2025-04-05 19:35:55 +0700
categories: tutorials jekyll

---

# Jekyll Objects and Variables Reference

## Global Site Variables (`site`)

```liquid
{{ site.title }}              # Site title from _config.yml
{{ site.description }}        # Site description
{{ site.url }}               # Site URL
{{ site.baseurl }}           # Site baseurl
{{ site.time }}              # Current time when site was built
{{ site.pages }}             # List of all Pages
{{ site.posts }}             # List of all Posts
{{ site.related_posts }}     # List of related posts
{{ site.categories.CATEGORY }}# Posts in category
{{ site.tags.TAG }}          # Posts with tag
{{ site.collections }}       # List of collections
{{ site.data.FILENAME }}     # Data from _data directory
{{ site.static_files }}      # Static files
{{ site.html_pages }}        # List of HTML Pages
{{ site.html_files }}        # List of static HTML files
{{ site.categories }}        # List of all categories
{{ site.tags }}             # List of all tags
```

## Page Variables (`page`)

```liquid
{{ page.content }}          # Page content
{{ page.title }}           # Page title
{{ page.excerpt }}         # Page excerpt
{{ page.url }}            # Page URL
{{ page.date }}           # Page date
{{ page.id }}             # Page identifier
{{ page.categories }}     # Page categories
{{ page.tags }}          # Page tags
{{ page.path }}          # Page source path
{{ page.next }}          # Next post object
{{ page.previous }}      # Previous post object
{{ page.excerpt }}       # Page excerpt
{{ page.draft }}         # True if page is a draft
{{ page.layout }}        # Page layout
```

## Post-Specific Variables (in addition to page variables)

```liquid
{{ post.date }}          # Post date
{{ post.categories }}    # Post categories
{{ post.tags }}         # Post tags
{{ post.title }}        # Post title
{{ post.url }}         # Post URL
{{ post.author }}      # Post author
{{ post.content }}     # Post content
{{ post.excerpt }}     # Post excerpt
{{ post.id }}         # Post identifier
```

## Paginator Object

```liquid
{{ paginator.page }}              # Current page number
{{ paginator.per_page }}         # Posts per page
{{ paginator.posts }}            # Posts on current page
{{ paginator.total_posts }}      # Total number of posts
{{ paginator.total_pages }}      # Total number of pages
{{ paginator.previous_page }}    # Previous page number
{{ paginator.previous_page_path }}# Previous page path
{{ paginator.next_page }}        # Next page number
{{ paginator.next_page_path }}   # Next page path
```

## Liquid Filters

### String Filters
```liquid
{{ "hello" | capitalize }}        # => "Hello"
{{ "hello" | upcase }}           # => "HELLO"
{{ "HELLO" | downcase }}         # => "hello"
{{ "hello world" | truncate: 5 }} # => "he..."
{{ "hello world" | slice: 0, 5 }} # => "hello"
```

### Array Filters
```liquid
{{ site.posts | sort: "title" }}
{{ site.posts | where: "category", "jekyll" }}
{{ site.posts | group_by: "category" }}
{{ site.posts | map: "title" }}
{{ array | first }}
{{ array | last }}
{{ array | join: ", " }}
{{ array | size }}
```

### Date Filters
```liquid
{{ post.date | date: "%B %d, %Y" }}
{{ site.time | date_to_string }}
{{ site.time | date_to_long_string }}
{{ site.time | date_to_rfc822 }}
{{ site.time | date_to_xmlschema }}
```

## Collection Objects

```liquid
{{ site.my_collection }}         # Access a collection
{{ collection.label }}          # Collection name
{{ collection.docs }}           # List of documents
{{ collection.files }}          # List of static files
{{ collection.relative_path }}  # Collection path
{{ collection.directory }}      # Collection directory
```

## Document Objects (in collections)

```liquid
{{ doc.content }}              # Document content
{{ doc.title }}               # Document title
{{ doc.url }}                # Document URL
{{ doc.path }}               # Document path
{{ doc.relative_path }}      # Document relative path
{{ doc.excerpt }}            # Document excerpt
```

## Example Usage Patterns

### 1. Iterating Through Posts
```liquid
{% for post in site.posts %}
  <article>
    <h2>{{ post.title }}</h2>
    <time>{{ post.date | date: "%B %d, %Y" }}</time>
    {{ post.excerpt }}
  </article>
{% endfor %}
```

### 2. Category Pages
```liquid
{% for category in site.categories %}
  {% capture category_name %}{{ category | first }}{% endcapture %}
  <h2>{{ category_name }}</h2>
  {% for post in site.categories[category_name] %}
    <article>
      <h3>{{ post.title }}</h3>
    </article>
  {% endfor %}
{% endfor %}
```

### 3. Navigation with Active Page
```liquid
{% for item in site.data.navigation %}
  <a href="{{ item.url }}" {% if page.url == item.url %}class="active"{% endif %}>
    {{ item.title }}
  </a>
{% endfor %}
```

### 4. Related Posts
```liquid
{% if site.related_posts.size >= 1 %}
  <div>
    <h3>Related Posts</h3>
    {% for related_post in site.related_posts limit: 3 %}
      <a href="{{ related_post.url }}">{{ related_post.title }}</a>
    {% endfor %}
  </div>
{% endif %}
```

### 5. Custom Collections with Metadata
```liquid
{% for project in site.projects %}
  <div class="project">
    <h2>{{ project.title }}</h2>
    <p>Tech Stack: {{ project.technologies | join: ", " }}</p>
    {{ project.content }}
  </div>
{% endfor %}
```

## Front Matter Options

```yaml
---
# Common Options
layout: post
title: "Post Title"
date: 2025-04-06
author: "Author Name"
categories: [category1, category2]
tags: [tag1, tag2]
permalink: /custom-url/

# SEO Options
description: "Page description"
keywords: "keyword1, keyword2"
image: /path/to/image.jpg

# Custom Variables
custom_var: "value"

# Collection Options
collection: projects
published: true
draft: false

# Pagination
pagination:
  enabled: true
  per_page: 10

# Multilingual
lang: en
translations:
  es: /es/page-url/
  fr: /fr/page-url/
---
```

## Advanced Liquid Syntax

### Conditional Logic
```liquid
{% if page.categories contains "jekyll" %}
  <p>This is a Jekyll post</p>
{% elsif page.categories contains "ruby" %}
  <p>This is a Ruby post</p>
{% else %}
  <p>This is another type of post</p>
{% endif %}
```

### Loops with Control
```liquid
{% for post in site.posts limit:5 offset:2 %}
  {{ post.title }}
{% else %}
  <p>No posts found</p>
{% endfor %}
```

### Variable Assignment
```liquid
{% assign sorted_posts = site.posts | sort: "title" %}
{% capture my_variable %}{{ "Hello" | upcase }}{% endcapture %}
```

### Including Templates
```liquid
{% include header.html %}
{% include custom.html param="value" %}
```

### Custom Filters
```liquid
{{ page.date | date: "%Y" | plus: 1 }}
{{ "string" | replace: "str", "new" }}
```

## Best Practices

1. **Use Front Matter Defaults**
   ```yaml
   # _config.yml
   defaults:
     -
       scope:
         path: ""
         type: "posts"
       values:
         layout: "post"
         author: "Default Author"
   ```

2. **Organize Data Files**
   ```yaml
   # _data/navigation.yml
   main:
     - title: "Home"
       url: "/"
     - title: "About"
       url: "/about/"
   ```

3. **Create Reusable Includes**
   ```liquid
   {% include post-card.html 
     title=post.title 
     date=post.date 
     excerpt=post.excerpt 
   %}
   ```

Remember that these objects and variables can be used in:
- Layouts (`_layouts/`)
- Includes (`_includes/`)
- Pages (any HTML/Markdown file)
- Posts (`_posts/`)
- Collection items
- Data files (`_data/`)

This reference should help you build more dynamic and feature-rich Jekyll sites! -->