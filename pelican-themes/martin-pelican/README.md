#Martin theme for Pelican static site generator

This is a port of the Martin theme by Allison House to work with the [Pelican static site generator](http://blog.getpelican.com/)

It supports the the following plugins or variables

- [Neighbor Article Plugin](https://github.com/getpelican/pelican-plugins/tree/master/neighbors)
- global variable GOOGLE_ANALYTICS for your Google Analytics ID.
- [font awesome](http://fortawesome.github.io/Font-Awesome/) for social and share links specified by global variables and the name of the font awesome icon after "fa-".
e.g.:
```
# Social widget
SOCIAL = (('github', 'http://github.com/username),
          ('twitter', 'http://twitter.com/username),
          ('instagram', 'http://instagram.com/username))

SHARE = (('twitter', 'http://twitter.com/share', '?text=', '&amp;url='),
         ('facebook', 'http://facebook.com/sharer.php', '?t=', '&amp;u='),
         ('google-plus', 'http://plus.google.com/share', '?text=', '&amp;url='))
```

- [Disqus](http://www.disqus.com) integration setting the variable
```
DISQUS_SITENAME = "your_site_name"
```

Showcase your project in style with Martin, a bold, timeless theme for GitHub pages! Named for the punchcutter William Martin, apprentice to John Baskerville. This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/). Check out the [live demo](http://cpaulik.github.io/martin-pelican/).

![Martin theme preview](https://raw.githubusercontent.com/cpaulik/martin-pelican/master/Pelican_martin_theme_preview.png)
