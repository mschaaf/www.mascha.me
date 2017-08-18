Framework for calculation and presentation of likelihoods
#########################################################
:date: 2007-11-03 14:19
:author: infram
:category: Misc
:tags: BachelorArbeit
:slug: framework-for-calculation-and-presentation-of-likelihoods
:status: published

My first addition to EzUnit is the implementation of a likelihood
framework. Needed things are a view that displays the likelihood for a
failure of a method, an extension point where different likelihood
calculation methods can be added and some methods for calculating a
likelihhod.

**Likelihood calculation**

I implemented four likelihood calculation methods. The first computes
the quotient from the count of failures and the count of all calls of a
method. The second calculates the test coverage of a method as the
quotient from the count of all calls and the sum of all method calls.
Then it calculates the failure likelihood and the passed likelihood as
quotient from failures/passes and the count of all calls of a method.
These three values are now taken to calculate the end likelihood in the
following way. A difference is build from the failure and passed
likelihood and this value is multiplied with the test coverage. This
method should rate methods higher that are more tested. The third and
the fourth are of the same type. They calculate a complexity of a method
by there length in characters. In the one hand it is calculated the
quotient from the length of method and the sum of the length of all
methods and on the other hand it is calculated the quotient from a
methods length and the length of the biggest method.

**Displaying the result**

The result is displayed as a tree. First comes the methods that have
possible failures and under this methods there come the test name from
where they called. Here it is defferenciated between failed and passed
tests. Then it is displayed a overall likelihood and under this overall
likelihood come all single likelihoods. The overall likelihood is
calculated as the sum from all likelihoods. All single likelihoods go in
this sum with the same weight.

**Rate likelihood methods**

To adjust the result you can vote or disable a likelihood method. A
method should be voted if it helps to find the failure. The user has to
decide when this is the case.
