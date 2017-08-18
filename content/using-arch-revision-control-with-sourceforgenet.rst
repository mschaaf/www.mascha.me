Using Arch Revision Control with Sourceforge.NET
################################################
:date: 2007-10-13 14:53
:author: infram
:category: Misc
:tags: Programming, revision control
:slug: using-arch-revision-control-with-sourceforgenet
:status: published

| 

Using Arch Revision Control with Sourceforge.NET
------------------------------------------------

by Martin Schaaf

1. Introduction
~~~~~~~~~~~~~~~

At home I use Arch since a long time and want to use it also for my
project hosted on sourceforge.net. So that I don't need to switch
between Arch and CVS any longer. My goal was to setup a mirror of my
local repository. That gives me the possiblity to develop locally and
commit my changes to the mirror in bigger time intervalls. I write it
down here because I think this can be interessting to other people too
and hope this will encourage other people to use arch with sf.net.

Other documents that refer to similar topics can be found on
`gna.org <https://gna.org/faq/?group_id=101&question=Arch_Server_--_How_do_I_setup_a_tla_archive.txt>`__
and
`wiki.gnuarch.org <http://wiki.gnuarch.org/Hosting_Arch_archive_on_Savannah_and_SourceForge>`__.

2. Result
~~~~~~~~~

As a result we will get a mirror of our archive on the sf.net project
web space. Where the project members can commit and others have readonly
access. The project member accesses the archive per sftp with the
following path

::

    sftp://<username>@<projectname>.sourceforge.net/home/<first_projectname_letter>/<first_two_projectname_letters>/<projectname>/htdocs/archives

The elements between the "<" and ">" brackets depends on the user it
accesses the project archive and the name of the project. To anonymous
access the project archive per http the following path can be used

::

    http://<projectname>.sourceforge.net/archives

3. Procedure
~~~~~~~~~~~~

Locally there is a signed archive called "a@b.c--sf-project" and we want
a mirror for a sf.net project called "projectname". It is created with

::

    tla make-archive --signed a@b.c--sf-project /home/a/archives/sf-project

and should be mirrored on sf.net. First we create the mirror with the
command

::

    tla make-archive --listing --mirror --signed a@b.c--sf-project sftp://a@projectname.sourceforge.net/home/p/pr/projectname/htdocs/archives

Now we have the mirror on sf.net. The next step is to register it
locally under a different archive name. We use for this step the command

::

    tla register-archive -d a@b.c--sf-project-MIRROR

The next and last step is to commit our local archive to the remote
sf.net archive. We use the following command

::

    tla archive-mirror a@b.c--sf-project a@b.c--sf-project-MIRROR

This have to be done everytime you want to update the mirror or can be
automatized to be done after every local commit. The Arch documentation
shows how to achive this.

4. Thanks
~~~~~~~~~

I will thank Tom Lord for developing this very nice and easy useable
revision control called Arch and Sourceforge.NET for providing free
project hosting.
