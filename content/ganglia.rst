Ganglia
#######
:date: 2008-05-10 07:00
:author: infram
:category: Misc
:tags: Programming
:slug: ganglia
:status: published

I had to install
`**Ganglia** <http://sourceforge.net/projects/ganglia/>`__ on ten boxes.
I downloaded the source package and followed the readme file. It helped
me very much until the point I got on all ten boxes gmond to run and on
one the web server. But what now? The web server hadn't displayed any
information. So I came to the point I need gmetad to collect all the
informations. I putted it on the web server box to the gmond start
script and added the configuration file. First you have to change the
gmetad port because the default installation has the same as gmond
configured. Then you have to set all boxes in the field *data\_source*
like

::

    data_source "cluster name" box1 box2 box3 box4 box5

then set the *grid\_name* like

::

    gridname "grid name"

The last step is to set the grid name also in the gmond configuration
like

::

    cluster {
        name = "cluster name"
        ...
    }

After these last steps
`**Ganglia** <http://sourceforge.net/projects/ganglia/>`__ and the web
interface are running well.

Summary for a working
`**Ganglia** <http://sourceforge.net/projects/ganglia/>`__ with GUI:

-  run gmond on every server
-  set the grid name in gmond.conf
-  run gmetad on the same server as the web interface
-  set all boxes that run gmond in gmetad.conf
-  set the cluster name in gmetad.conf

The tool `**Cssh** <http://clusterssh.wiki.sourceforge.net/Main+Page>`__
helped me very much on doing the installation on all ten boxes in
parallel.
