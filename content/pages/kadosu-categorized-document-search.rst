KaDoSu - categorized document search
####################################
:date: 2007-10-14 18:48
:author: infram
:slug: kadosu-categorized-document-search
:status: published

What was the problem
^^^^^^^^^^^^^^^^^^^^

I was at a point where I had collected many many documents (manuals,
howtos, specs, ...). In many many different formats (ps, pdf, sxw, tgz,
zip, ...). And in many many directories. A search with find and grep
doesn't help me here. My tries to categorize these documents end at a
point where I don't find documents because I searched at the wrong
categories. :( A friend of mine had the same problems on his OS. We have
not found any helpfull application. So we decided to implement our own.
The so called KaDoSu.

What does it
^^^^^^^^^^^^

It indexes all documents in an archive and let you search in the index.
It automatically categorizes the search results and let the user
manually categorize a document. It visualises the search results textual
and graphical. The Eclipse RCP is used to programm Kadosu. Kadosu is
written in Java and easily extentable.

How
^^^

KaDoSu differentiates between documents and archives (similar to files
and directories). An archive can consist of archives and/or documents. A
document consists of text only.

Goals
^^^^^

-  easy to add new documents and archives
-  easy to add new indexer
-  easy to add new analyzer (for lucene)
-  automatic and manual categorization of search results
-  run on different platforms
-  graphical and textual visualisation of the search results
-  use as many as possible existing tools and libraries
-  ...

News
^^^^

News will be posted under the category
`kadosu <http://infram.wordpress.com/category/kadosu/>`__.

Tools
^^^^^

-  Java (http://www.java.com/)
-  Eclipse Rich Client Platform (http://www.eclipse.org/)
-  Jakarta Lucene (http://jakarta.apache.org/lucene/index.html)

Download
^^^^^^^^

https://launchpad.net/kadosu/

Screenshot
^^^^^^^^^^

Java and all Java-based trademarks are trademarks of Sun Microsystems,
Inc. in the United States, other countries, or both. Other company,
product, and service names may be trademarks or service marks of others.

