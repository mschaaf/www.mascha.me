How to change the default UserAgent value in Konqueror
######################################################
:date: 2007-06-12 13:55
:author: infram
:category: Misc
:slug: how-to-change-the-default-useragent-value-in-konqueror
:status: published

I want to change the UserAgent string in Konqueror fore every site visit
and not only for a special site. But the interface has not such
functionality. It is possible to set it directly in the following file
*~/.kde/share/config/kio\_httprc* by adding the following string on the
first line in this file *UserAgent=<newAgentName>*. NewAgentName has to
be replaced by the wished name.
