#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Martin Schaaf'
SITENAME = 'mascha.me'
SITEURL = 'http://singer-polecat-50631.netlify.com'
SITESUBTITLE = 'programming languages and surroundings'
DISPLAY_CATEGORIES_ON_MENU = False
SINGLE_AUTHOR = True

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Do not publish articles set in the future
WITH_FUTURE_DATES = False
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Blogroll
LINKS = (
    ('Dica-Developer', 'https://github.com/Dica-Developer'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/maschahcsam'),
    ('linkedin', 'https://www.linkedin.com/in/martinschaaf'),
    ('github', 'https://github.com/mschaaf'),
    ('google-plus', 'https://plus.google.com/106994785762247226147')
)

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_PAGINATION = 25
PAGINATED_DIRECT_TEMPLATES = ('blog-index',)
DIRECT_TEMPLATES = ('tag', 'index', 'blog-index', 'blog')
TEMPLATE_PAGES = {'blog.html': 'blog.html'}

POST_LIMIT = 25

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-themes/BT3-Flat'
#THEME = 'pelican-themes/chunk'

#===theme settings===========================
FAVICON = ''
ICON = ''
SHORTCUT_ICON = ''
HEADER_IMAGE = ''
BACKGROUND_IMAGE = 'images/background.jpg'

ARTICLES_HOME_PAGE = False

PERSONAL_PHOTO = 'https://avatars2.githubusercontent.com/u/703355?v=4&s=400'
PERSONAL_INFO = 'dfsfs dfds fd dg dg'

WORK_DESCRIPTION = 'dfdfg df dg dg'
WORK_LIST = (
    ('link', 'https://dl.dropboxusercontent.com/u/299446/BT3-Flat.png', 'BT3-Flat', 'A BT3 flat theme for pelican', 'https://github.com/KenMercusLai/plumage')
)

