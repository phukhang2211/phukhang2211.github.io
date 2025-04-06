---
layout: post
title: "Jekyll Objects and Variables Quick Reference"
date: 2025-04-06
categories: jekyll reference
tags: [liquid, objects, guide]
excerpt: "A comprehensive reference for Jekyll objects, variables, and filters"
---

# Jekyll Objects Quick Reference

## Site Variables
- `site.title` - Your site's title
- `site.description` - Site description
- `site.url` - Site URL
- `site.baseurl` - Site base URL
- `site.time` - Current build time
- `site.pages` - All pages
- `site.posts` - All posts
- `site.categories` - All categories
- `site.tags` - All tags

## Page Variables
- `page.title` - Page title
- `page.date` - Page date
- `page.url` - Page URL
- `page.content` - Page content
- `page.categories` - Page categories
- `page.tags` - Page tags
- `page.excerpt` - Page excerpt
- `page.next` - Next post
- `page.previous` - Previous post

## Post Variables
- `post.title` - Post title
- `post.date` - Post date
- `post.url` - Post URL
- `post.categories` - Categories
- `post.tags` - Tags
- `post.content` - Content
- `post.excerpt` - Excerpt

## Common Filters
```liquid
# Text
{% raw %}{{ "hello" | capitalize }}{% endraw %}
{% raw %}{{ "hello" | upcase }}{% endraw %}
{% raw %}{{ "HELLO" | downcase }}{% endraw %}

# Arrays
{% raw %}{{ array | first }}{% endraw %}
{% raw %}{{ array | last }}{% endraw %}
{% raw %}{{ array | size }}{% endraw %}

# Dates
{% raw %}{{ post.date | date: "%Y-%m-%d" }}{% endraw %}
```

## Usage Examples

### List Posts
```liquid
{% raw %}{% for post in site.posts %}
  {{ post.title }}
{% endfor %}{% endraw %}
```

### Show Categories
```liquid
{% raw %}{% for category in site.categories %}
  {{ category[0] }}  # Category name
  {% for post in category[1] %}
    {{ post.title }}
  {% endfor %}
{% endfor %}{% endraw %}
```

### Navigation
```liquid
{% raw %}{% for item in site.data.navigation %}
  <a href="{{ item.url }}">{{ item.title }}</a>
{% endfor %}{% endraw %}
```

## Front Matter Template
```yaml
---
layout: post
title: "Your Title"
date: YYYY-MM-DD
categories: [cat1, cat2]
tags: [tag1, tag2]
author: "Your Name"
excerpt: "Brief description"
---
```

## Tips
1. Use `site` for global info
2. Use `page` for current page
3. Use `post` in post loops
4. Categories/tags are arrays
5. Always include front matter
6. Use filters to format output

## Common Tasks

### Category Pages
```liquid
{% raw %}{% for post in site.categories.your-category %}
  {{ post.title }}
{% endfor %}{% endraw %}
```

### Related Posts
```liquid
{% raw %}{% for post in site.related_posts limit:3 %}
  {{ post.title }}
{% endfor %}{% endraw %}
```

### Date Formatting
```liquid
{% raw %}{{ page.date | date: "%B %-d, %Y" }}{% endraw %}
```

### Includes with Parameters
```liquid
{% raw %}{% include component.html param="value" %}{% endraw %}
```

Remember:
- Use {% raw %}`{{ }}`{% endraw %} for output
- Use {% raw %}`{% %}`{% endraw %} for logic
- Front matter between `---`
- Use proper date format
- Categories/tags in arrays
- Keep URLs clean
