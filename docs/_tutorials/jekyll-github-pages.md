---
layout: post
title: "How to Create a Blog with Jekyll and GitHub Pages"
category: beginner
date: 2025-04-06
excerpt: "Step-by-step guide to setting up a blog using Jekyll and GitHub Pages"
---

# Creating a Blog with Jekyll and GitHub Pages

This guide will walk you through setting up a blog using Jekyll and hosting it on GitHub Pages.

## Prerequisites

- Ruby installed on your computer
- Git installed
- GitHub account
- Basic knowledge of Markdown

## Step 1: Initial Setup

1. Install Jekyll and Bundler:
```bash
gem install jekyll bundler
```

2. Create a new Jekyll site:
```bash
jekyll new your-username.github.io
cd your-username.github.io
```

3. Initialize Git and link to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
```

## Step 2: Directory Structure

Your Jekyll site should have this structure:
```
your-username.github.io/
├── _config.yml          # Site configuration
├── _posts/             # Blog posts
├── _projects/          # Project collection
├── _tutorials/         # Tutorial collection
├── _layouts/           # Custom layouts
├── _data/             # Data files (navigation, etc)
├── assets/            # Images, CSS, JS files
│   ├── images/
│   ├── css/
│   └── js/
└── index.markdown      # Homepage
```

## Step 3: Configuration

Edit `_config.yml` with your settings:
```yaml
title: Your Blog Title
email: your-email@example.com
description: >- 
  Write your site description here.
baseurl: "" # for user site
url: "https://username.github.io"

# Collections
collections:
  projects:
    output: true
    permalink: /projects/:path/
  tutorials:
    output: true
    permalink: /tutorials/:path/

# Build settings
theme: minima
plugins:
  - jekyll-feed
```

## Step 4: Creating Content

### Blog Posts
Create posts in `_posts/` with format: `YYYY-MM-DD-title.md`
```yaml
---
layout: post
title: "Your Post Title"
date: 2024-04-05
---

Your content here...
```

### Projects
Add projects in `_projects/` (no date required):
```yaml
---
layout: post
title: "Project Name"
excerpt: "Project description"
---

Project details here...
```

### Tutorials
Add tutorials in `_tutorials/`:
```yaml
---
layout: post
title: "Tutorial Title"
category: beginner
---

Tutorial content here...
```

## Step 5: Local Development

1. Run locally:
```bash
bundle exec jekyll serve
```

2. View at: `http://127.0.0.1:4000`

## Step 6: Deploy to GitHub Pages

1. Create a new repository named `username.github.io`

2. Push your code:
```bash
git remote add origin https://github.com/username/username.github.io.git
git branch -M main
git push -u origin main
```

3. Enable GitHub Pages:
   - Go to repository Settings
   - Navigate to Pages section
   - Select Deploy from a branch
   - Choose main branch and save

Your site will be live at: `https://username.github.io`

## Tips and Tricks

### Adding Images
```markdown
![Image Alt Text](/assets/images/image.jpg)
```

### Creating Links
```markdown
[Link Text](URL)
```

### Code Blocks
````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

### Front Matter Variables
```yaml
---
layout: post
title: "Your Title"
date: 2024-04-05
categories: [web, tutorial]
tags: [jekyll, github-pages]
author: Your Name
---
```

## Common Issues and Solutions

1. **Missing Dependencies**
   ```bash
   bundle install
   ```

2. **Page Build Failed**
   - Check _config.yml syntax
   - Verify front matter format
   - Look for missing dependencies

3. **CSS Not Loading**
   - Check baseurl in _config.yml
   - Verify asset paths

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/pages)
- [Markdown Guide](https://www.markdownguide.org/)

## Next Steps

1. Customize your theme
2. Add comments using Disqus
3. Set up Google Analytics
4. Create custom layouts
5. Add search functionality

Remember to commit and push changes regularly to keep your site updated!