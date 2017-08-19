Specification for filtering text output of plugins
##################################################
:date: 2009-02-04 12:12
:author: infram
:slug: specification-for-filtering-text-output-of-plugins
:status: published

**Filter**

Filter should parse text ouptut of plugins. And as a result add new
fields based on this output to a document.

Filter should be used for fields that are common to more then one
plugin. E.g. to add a language field. So that not every plugin has to
provide the functionality to determine the content language. But it
should have the possiblity to do this in case it is faster or more
reliable or ... To achieve this a filter only adds new fields to a
document and does not overwrite fields from a plugin.

**Improvements**

For good performance plugins should expose the fields they set. So that
filters doesn't get called in case they would not add filters. And that
filters only get called for fields that need to be set.
