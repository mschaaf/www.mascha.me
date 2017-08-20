# dev-random3 #

This theme is a fork of [dev-random](https://github.com/getpelican/pelican-themes/tree/master/dev-random) by Sam Hocevar.

It contains templates for :

- archives
- article
- author
- category
- tag
- language

## 404 ##

It has also a simple 404 error page. In order to use it, you have to add '404' in your direct templates conf

*DIRECT_TEMPLATES = (... ,'404')*

Then in nginx :

*error_page 404 /404.html*

I don't know for others like Apache, but it should be easy to find. Please write to me and I will add the thing.

## Sidebar ##

I refactored the sidebar. If you want to move up or down the widget pieces, you just have to move up and down each piece of three code line in the sidebar.html template.

{% if categories %}  
{% include "sidebar.d/categories.html" %}  
{% endif %}  

You can also move the tag cloud.

## Links ##

I placed a links widget. In order to use it, you have to include it in your conf like :

LINKS =  (('http://www.22decembre.eu','photos de 22decembre'),   
	...  
	('url','linkname'),)  
	
## CAcert ##

If you have a cacert enabled website, and want to show it to visitors, let them come with https or not, you can just placed

CACERT = True

in your pelicanconf.

You need also (currently) BAREURL, which show your bare url, without the http. In my case, it gives

BAREURL = 'www.22decembre.eu'

## Language ##

This theme was specially customized for use with the [lang-category](https://github.com/CNBorn/pelican-langcategory) plugin, which I ask just a bit for and worked a bit with the dev' on.

This is my config, slightly different from the base plugin (I don't use the word 'lang' in the url itself) :

PLUGINS = [... "pelican-langcategory"]

LANGUAGES= (('code','name', 'url'),
	    ('fr','french', 'fr'),
	    ('en','english','en'),)

LANGUAGE_URL = '{lang}/'  
LANGUAGE_SAVE_AS = '{lang}/index.html'  

PAGE_URL = "{lang}/{slug}.html"  
PAGE_SAVE_AS = "{lang}/{slug}.html"  
PAGE_LANG_URL = "{lang}/{slug}.html"  
PAGE_LANG_SAVE_AS = "{lang}/{slug}.html"  

## Live demo ##

The best demo is the author's website : [www.22decembre.eu](http://www.22decembre.eu)
