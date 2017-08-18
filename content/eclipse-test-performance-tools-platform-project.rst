Eclipse Test & Performance Tools Platform Project
#################################################
:date: 2007-09-07 15:19
:author: infram
:category: Misc
:tags: BachelorArbeit
:slug: eclipse-test-performance-tools-platform-project
:status: published

I had to try this Eclipse project out. On trying it I got every time the
error that the profiler agent cannot be accessed, becaused it isn't
started. But I need this project running and had to find the problem. I
use Eclipse 3.3 on Ubuntu Linux 7.04. First I find the scripts on
starting the agent server in
*/eclipse/plugins/org.eclipse.tptp.platform.ac.linux\_ia32\_4.4.0.v200706020100/agent\_controller/bin*
and found out that they are missing the execute rights. Then I started
the script by hand *./ACStart.sh* and get the following error *[: 46:
==: unexpected operator*. The solution is to set in the first line the
interpreter to bash instead of sh, because Ubuntu uses a small
replacment for the bash called dash. Again. Now I get a new error that's
saying *libtptpUtils.so.4 needs /usr/lib/libstdc++-libc6.2-2.so.3*.
Where to get this library? After some web searching I found out that I
had to install the following package *libstdc++2.10-glibc2.2*. Now the
agent starts. Let's start profiling.
