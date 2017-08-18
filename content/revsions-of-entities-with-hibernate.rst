Revisions of entities with hibernate
####################################
:date: 2009-03-04 09:25
:author: infram
:category: Misc
:tags: entity, envers, hibernate, persistence, Programming, revisions
:slug: revsions-of-entities-with-hibernate
:status: published

The last week we implemented revisions for entites with
`hibernate <http://www.hibernate.org/>`__. We decided us for
`envers <http://www.jboss.org/envers/>`__. `The
documentation <http://www.jboss.org/files/envers/docs/index.html>`__ is
good. We were able to get a working revision system with switching
between revisions within this week. One note we used the version
1.1.0.GA for hibernate 3.2.6 so the documentation didn't applied fully
the naming of annotations and configuration property names changed. We
run in to one issue. Our database already existed and we had to
introduce the revisions later. Envers does not create on first run a
initial revision for versioned entities. But you will need them because
if you switch back you will lost data for properties that are stored in
a list. Lets say you have a versioned entity with a list of strings and
you change this list by adding entries. If you go back you don't have
the entries that were in the list before you added the new one. To solve
this we had to write our own tool to create the first revision. Since
fixing this envers works very good in our project. I can suggest its
usage.
