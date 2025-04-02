#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kane'
SITENAME = "Kane's Blog"
SITEURL = ''
SITESUBTITLE = 'Python, GIS, and Web Development'

PATH = 'content'
OUTPUT_PATH = 'output'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['']

# Timezone and Language
TIMEZONE = 'Asia/Ho_Chi_Minh'
DEFAULT_LANG = 'vi'
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

# Feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Menu Items
MENUITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
)

# Blogroll
LINKS = (
    ('Pymi', 'https://pymi.vn/'),
    ('Familug', 'https://www.familug.org/'),
    ('Python.org', 'https://www.python.org/'),
    ('Pelican', 'https://getpelican.com/'),
)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/phukhang2211'),
)

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

# Theme settings
THEME = 'notmyidea'
STATIC_PATHS = ['images']

# Plugins and Extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'permalink': True},
    },
    'output_format': 'html5',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True 