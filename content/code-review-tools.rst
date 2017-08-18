code review tools
#################
:date: 2014-03-07 07:48
:author: infram
:category: Misc
:tags: code review, developement, software
:slug: code-review-tools
:status: published

After the last critical and prominent software bugs
[`1 <http://mascha.me/2014/03/07/critical-crypto-bug-leaves-linux-hundreds-of-apps-open-to-eavesdropping-ars-technica-lwn-net/>`__ , `2 <http://mascha.me/2014/03/02/goto-fail-considered-harmful-lwn-net/>`__] that
could be avoided by code review. I will name some of them and write one
or two sentence about it.

In my current development work I had to check commits, packages/modules.
This leads to the differentiation between commit review and technical
reviews. We used commit reviews to find any sort of bug but it is hard
to find design problems in inspecting only a commit without knowing the
rest of the code so introduced technical reviews that watched whole
classes and packages. We do commit reviews daily and technical reviews
after introducing a feature and by request. The following tools help us
by doing these types of reviewing.

`Sonarqube <http://www.sonarqube.org/>`__\  is full featured code
analyzing tool and one part of it is allowing to comment on your code.
With this feature you can do technical reviews.

`Barkeep <https://github.com/ooyala/barkeep>`__ is review
tool specialized on commit reviews. It does this and does it very well.

`Pair
Programming <http://www.extremeprogramming.org/rules/pair.html>`__ is
not a tool it is a rule of `extreme
programming <http://www.extremeprogramming.org>`__ but I find it very
helpful to avoid bugs before you commit your code.

What I already missed so far is a tool that integrates well both review
types. So a `group of developers <https://github.com/Dica-Developer>`__
(I am part of it) started a tool with name
`gh-review <http://dica-developer.github.io/gh-review/>`__ that tries to
combine both.
