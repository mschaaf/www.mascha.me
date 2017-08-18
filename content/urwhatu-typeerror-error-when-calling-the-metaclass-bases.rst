TypeError: Error when calling the metaclass bases
#################################################
:date: 2010-01-10 14:28
:author: infram
:category: Misc
:tags: Programming, python, python for java programmers
:slug: urwhatu-typeerror-error-when-calling-the-metaclass-bases
:status: published

`This
article <http://andre.stechert.org/urwhatu/2005/03/typeerror_error.html>`__
helped me by fixing this exception. The following code gave this
exception

::

    ...
    from a import A
    class B (A):
    ...

but this was wrong because my class had the same name as the file it was
in. This meant that my class had the same name as the module. To make it
right it should be:

::

    ...
    from a import A
    class B (A.A):
    ...
