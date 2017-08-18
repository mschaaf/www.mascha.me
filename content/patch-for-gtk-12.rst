Patch for gtk+ 1.2
##################
:date: 2007-10-13 14:53
:author: infram
:category: Misc
:tags: c, gtk, heap sort, patch, Programming, sort
:slug: patch-for-gtk-12
:status: published

Heap sort for the GTK+ ctree widget

It was mainly written for Sylpheed-claws but should implemented in the
lib not in the app. So here is the patch
(`gtk+-ctree-sorting.patch.gz <http://www.ma-scha.de/download/gtk+-ctree-sorting.patch.gz>`__).

| For GTK+ version: 1.2.10
| Gprof timings for about 20000 entries:

::

    function            new     old
    gtk_ctree_unlink    0.03s   0.74s
    gtk_ctree_link      0.01s   0.55s
    compare             0.01s   1.18s
    sort algorithm      0.04s   3.94s
    sum                 0.09s   6.41s
