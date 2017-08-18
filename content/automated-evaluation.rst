Automated evaluation
####################
:date: 2007-11-14 16:12
:author: infram
:category: Misc
:tags: BachelorArbeit, Programming
:slug: automated-evaluation
:status: published

How to evaluate? First my colleagues should only test it. But my
professor thought that this isn't enough for an expressive and
compareable result. So the idea is to set errors and start the
evaluation when tests fail. And everything should work automatically.
The user start it and after a month or so you have the result without
any intervention by the user

**Jesting**

There exists a tool called `Jester <http://jester.sourceforge.net/>`__
that changes the source code of programms and run the tests after every
change. If no tests fail it will remember the position and what changed.
With this procedure it is possible to find source code that isn't well
tested. But this isn't exactly what we need. We need failed tests to
test how good an evaluator finds the changed method.

**EzUnit and Jester**

The procedure is as follow. First we get all methods of a projects
source folder from the Eclipse (JDT). Then we do one style of change,
there are 11 variants of changing the source code, after each other for
every method. These variants are taken from Jester. I will explain them
later. Then the test suite is started. If compilation is necessary the
launch waits for completion and continues thereafter. There are three
cases after the test site launch. Junit can give an error back this
means something not test specific goes wrong. In the case Junit returns
with a failure the evaluation is started because thento reverse there
are failed tests. The third case is that nothing failed after the
change. Then there is nothing to evaluate like after an error and you
know that there is bad tested code in the project. The next step is to
take all made changes back. If all methods are changed with all variants
of source code changes a csv file is written with all results in the
project root folder.

**Changing source code**

Jester has 11 variant of changing source code. All are implemented by
EzUnit. There is an number changer that searches for one digit and add 1
to it. This Jester implementation can lead to compilation errors because
it changes an octal number representation from 0x ... to 1x... If such a
change happens it is ignored. The other methods replace java language
constructs to reverse there meaning like "true" to "false", "if (" to
"if (true \|\|", "if (" to "if (false &&", "==" to "!=", "!=" to "==",
"++" to "−−" and "−−" to "++". Such changes can lead to endless loops.
To avoid an ever blocking test the timeout annotation (@Test(timeout =
60000) for Junit4 should be used. But we saw also endless loops where
the cause is unknown for now and where the setting of the timeout are
not working. In this cases the launch has an timeout set so that it
continues with another change.

**The time**

First tests show that a evaluation run can take very long dependent on
the number of methods and tests a project has and the time for one test
run. An evaluation run with commons-codec (191 tests) needs 4 hours on
double processor with 1.66GHz and for commons-math (1022 tests) about 4
days.
