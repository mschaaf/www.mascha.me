Cyclomatic Complexity
#####################
:date: 2007-11-24 13:20
:author: infram
:category: Misc
:tags: BachelorArbeit, complexity, cyclomatic complexity, McCabe
:slug: cyclomatic-complexity
:status: published

`Cyclomatic
Complexity <http://en.wikipedia.org/wiki/Cyclomatic_complexity>`__ is
added as a new approach to find methods that are possible failures. It
is implemented in the way that McCabe describes it in its `original
paper <http://www.literateprogramming.com/mccabe.pdf>`__ on page 7 and
8. The cyclomatic complexity number is computed by counting all if, for
and which statements of a method. For every if statement that contains a
*&&* 2 is add to the cyclomatic complexity.

**Complex**

The cyclomatic complexity doesn't have a maximum value but the
likelihood evaluator has to return a value between 0 and 1 including 0
and 1. To have a maximum for converting the cyclomatic complexity
between 0 and 1 complexity values bigger than 10 are set to 10. This is
the upper bound that McCabe terms in his paper on page 7.

**Case statements**

McCabe says in his paper on page 9: "The only situation in which this
limit has seemed unreasonable is when a large number of independent
cases followed a selection function (a large case statement), which was
allowed." To have a "reasonable" upper limit the case statements aren't
count.

**Enhancements**

To have a complete implementation of the cyclomatic complexity
measurement the case statements should also be taken in account, but
then it should be possible to configure the upper limit.
