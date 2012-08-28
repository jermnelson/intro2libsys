==================
Indexing with Solr
==================
`Solr`_ is an open-source project sponsored by the Apache software
foundation and is based on the full-text `Lucene`_ project but is
easier to set-up and use. Solr is used by multiple different open-source
and commercial library systems including `Blacklight`_, `VuFind`_,
`Aristotle`_, `Koha`_, and `Bibliocommons`_.

Overview
--------
Solr is written in the Java programming language and offers full-text 
indexing of plain text, PDFs, and common office formats like Microsoft
Word documents. A popular Java-based open-source library called `Solrmarc`_,
is used by Blacklight and VuFind to index MARC21 and MARC XML into a Solr
index. Other uses of Solr in library systems include indexing Dublin Core and
MODS meta-data records and Solr may be used for information discovery in 
document management systems in corporations and other organizations.


Using Solr
----------
Solr is relatively easy to set-up and get up and running. The challenge of
configuring the index and the query parsers is not for the faint hearted
as Solr installations can quickly become complex in meeting users 
information searching requirements. 

Solr Components 
--------------
Solr is an extendable technology, meaning that various subsystems can be
changed or modified to meet a particular need or requirement. 

Core and Multicore
^^^^^^^^^^^^^^^^^^
A simple Solr installation has a single Core that allows documents to be added
or deleted while running. Solr ensures that documents are unique by requiring
each document to have an ID that is unique through the core. Solr also offers
duplicate document detection, customizable request handlers, and user commands. 

Solr also offers a multicore set-up that allows a single Solr installation to
have multiple cores, each with its own schema and set-up, that can be searched
from a single server. For example, a library solr installation may have a core
for MARC records and a separate core its MODS and Dublin Core documents but
the server can still be searched from a single interface. 

Schema, Solrconfig, Stopwords, and Synonyms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Solr schema is an XML configuration file that defines the fields and
field types in the index. Through the use of the CopyField element, composite
fields can be built from multiple fields or a single field can be parsed into
separate fields. This is useful, for example, to have one field that is 
composed of all the text or data in a document while offering different and
specific fields for different types of search queries or weightings.

The Solrconfig is another critical XML configuration file where the different
types of queries are included. These queries, called request handlers, allow
for only certain fields to be searched along with weightings to change the 
relevance rankings of documents in the search results. For example, specific
types of Title, Author, or Subject searches can be easily supported in the
solrconfig file by defining a request handler for each of those types of 
searches along with different weights associated with those fields.

Solr also supports the use of stopwords (common words like "a", "an", "the", that are ignored by the index and from which its inclusion can result in more 
false hits when a user includes them in a search query. Likewise, the synonyms 
file or files allow for broader or narrow associations between terms which can
improve the search result relevance by the end user.  

References
----------

.. _Aristotle: https://github.com/jermnelson/Discover-Aristotle
.. _Bibliocommons: http://www.bibliocommons.com/
.. _Blacklight: http://projectblacklight.org/
.. _Koha: http://www.koha.org/
.. _Lucene: http://lucene.apache.org/
.. _Solr: http://lucene.apache.org/solr/
.. _Solrmarc: http://code.google.com/p/solrmarc/
.. _VuFind: http://vufind.org/
