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
    ("Don Brown's Weblog", 'http://jroller.com/mrdon/'),
    ("doobop’s soup", 'http://doobop.soup.io/'),
    ('eighty-eight myles per hour', 'https://bethesignal.org/'),
    ('M A M B L O G', 'http://mam-foto.blogspot.com/'),
    ("Marcus-Andreas Mohr’s Blog", 'http://marcusandreasmohr.wordpress.com/'),
    ('0xmb', 'http://mbauhardt.github.io/'),
    ('SuzieSoup', 'http://suzie.soup.io/'),
    ("oae's Blog", 'https://oae9.wordpress.com/'),
    ('Schneier on Security', 'http://www.schneier.com/blog/'),
    ('The Sietch Blog', 'http://www.blog.thesietch.org/'),
    ('Tom Yam', 'http://robert.soup.io/'),
    ('UX Crank', 'http://www.dswillis.com/uxcrank/'),
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
PAGINATED_DIRECT_TEMPLATES = ('blog',)
DIRECT_TEMPLATES = ('index', 'blog',)
#TEMPLATE_PAGES = {'blog.html': 'blog.html'}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-themes/BT3-Flat'

#===theme settings===========================
FAVICON = ''
ICON = ''
SHORTCUT_ICON = ''
HEADER_IMAGE = ''
BACKGROUND_IMAGE = 'images/background.jpg'

ARTICLES_HOME_PAGE = False

PERSONAL_PHOTO = 'https://avatars2.githubusercontent.com/u/703355?v=4&s=400'
PERSONAL_INFO = 'child and developer'

WORK_DESCRIPTION = 'developed'
WORK_LIST = (
    ('link', '', 'All', '', 'pages/index.html'),
)

