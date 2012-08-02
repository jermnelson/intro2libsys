===========
Dublin Core
===========
`Dublin Core`_ offers a core set of meta-data vocabularies for describing
simple and generic resource descriptions. `Dublin Core`_ has four levels
of interoperability, range from the most basic at level one up to the most
rigorous level of interoperability at level four. But what does this mean
in practice? If two resources are described at a specific level, then the
system designer can be assured of certain statements about them are correct
for both.  These resources can be used together without much manipulation
overhead to normalize them in a constant fashion. Think of the issues involved
(which comes more often then you would think) if different communities understand
and conceptualize a concept in different fashions. For example, an
editor of a monograph could be classified as either a Dublin core
contributor, publisher, or creator depending on the use case or common
practice. This makes it difficult to normalize searching and representation
in a single system that uses records from these different communities.

Level One interoperability, called Shared term definitions [#]_ is the 
simplest or most basic level which is what most web pages use. This level
primarily uses the 15 core elements of the following:

*. contributor  - an individual or organization that contributed in some
   way to resource. [#]_
   
*. coverage - a temporal or spacial topic associated or assigned to the
   resource. [#]_

*. creator - an individual, group, organization, or server who is the
   primary entity responsible for creation of the resource. [#]_

*. date - a single point or date range associated with the resource, such
   as a copyright date. [#]_
   
*. description - an textual or graphical account of the resource, includes such 
   things as an abstract, graphic, or free-text. [#]_
   
*. format - the physical medium, file type, or other descriptive phrase 
   such as dimensions of the resource. [#]_
   
*. identifier - a specific and unambiguous reference to the resource within
   a certain context like an ISBN number of a monograph, an ISSN number
   of a serial or magazine, or a URL for a web-page. [#]_
   
*. language - the human language of the resource. [#]_

*. publisher - the individual, group, or organization that makes the
   resource accessible or available. [#]_
   
*. relation - a different resource that is related in some way to the 
   original resource. Examples include a different issue of a serial,
   an older edition of a monograph, or another work by the same creator. [#]_
   
*. rights - the conditions or restriction on use, availability or 
   other rights about the resource including licenses or copyrights. [#]_
   
*. source - the original source material or resource from which the currently
   described resource is derived from or inspired by. [#]_
   
*. subject - the topic or keyword associated with the resource. Can
   be part of a controlled vocabulary. [#]_
   
*. title - name or other phrase that is commonly or formally
   associated with the resource. [#]_
   
*. type - the genre or other term, usually from a controlled vocabulary,
   that classifies the resource. [#]_

Level Two interoperability, or formal semantic interoperability [#]_ is the next
level of Dublin Core and means that resources use shared vocabularies structured
using formal semantics. Level Two is used as a bases for `RDF`_ and 
`Linked Data`_ efforts and is the base descriptive set for many Semantic
Web efforts. We will go into more detail about this level of Dublin Core
interoperability in the `RDF`_ and `Linked Data`_ sections.

Level Three, Description Set syntactic interoperability, [#]_ and Level 
Four, Description Set Profile interoperability [#]_ are similar in that
beyond just a formal semantics, these levels provide better validation 
for exchanging meta-data records within certain parameters, or bounded set,
including conventions for representing and identifying the records. The 
difference between level three and four is more to do with the how the
interoperability is achieved. A system with its own methods of validation
may reach level three but a system using a Dublin Core XML constraint
language for validation and exchange would be a level four.


Pros
----

Cons
----

References
----------

.. [#] `Level 1: Shared term definitions`_
.. [#] `Dublin Core contributor Definition`_
.. [#] `Dublin Core coverage Definition`_
.. [#] `Dublin Core creator Definition`_
.. [#] `Dublin Core date Definition`_
.. [#] `Dublin Core description Definition`_
.. [#] `Dublin Core format Definition`_
.. [#] `Dublin Core identifier Definition`_
.. [#] `Dublin Core language Definition`_
.. [#] `Dublin Core publisher Definition`_
.. [#] `Dublin Core relation Definition`_
.. [#] `Dublin Core rights Definition`_
.. [#] `Dublin Core source Definition`_
.. [#] `Dublin Core subject Definition`_
.. [#] `Dublin Core title Definition`_
.. [#] `Dublin Core type Definition`_
.. [#] `Level 2: Formal semantic interoperability`_
.. [#] `Level 3: Description Set syntactic interoperability`_
.. [#] `Level 4: Description Set Profile interopability`_

.. _Dublin Core: http://dublincore.org/
.. _Dublin Core contributor Definition: http://dublincore.org/documents/dces/#contributor
.. _Dublin Core coverage Definition: http://dublincore.org/documents/dces/#coverage
.. _Dublin Core creator Definition: http://dublincore.org/documents/dces/#creator
.. _Dublin Core date Definition: http://dublincore.org/documents/dces/#date
.. _Dublin Core description Definition: http://dublincore.org/documents/dces/#description
.. _Dublin Core format Definition: http://dublincore.org/documents/dces/#format
.. _Dublin Core identifier Definition: http://dublincore.org/documents/dces/#identifier
.. _Dublin Core language Definition: http://dublincore.org/documents/dces/#language
.. _Dublin Core publisher Definition: http://dublincore.org/documents/dces/#publisher
.. _Dublin Core relation Definition: http://dublincore.org/documents/dces/#relation
.. _Dublin Core rights Definition: http://dublincore.org/documents/dces/#rights
.. _Dublin Core source Definition: http://dublincore.org/documents/dces/#source
.. _Dublin Core subject Definition: http://dublincore.org/documents/dces/#subject
.. _Dublin Core title Definition: http://dublincore.org/documents/dces/#title
.. _Dublin Core type Definition: http://dublincore.org/documents/dces/#type
.. _`Level 1: Shared term definitions`: http://dublincore.org/documents/interoperability-levels/#sect-2
.. _`Level 2: Formal semantic interoperability`: http://dublincore.org/documents/interoperability-levels/#sect-3
.. _`Level 3: Description Set syntactic interoperability`: http://dublincore.org/documents/interoperability-levels/#sect-4
.. _`Level 4: Formal semantic interoperability`: http://dublincore.org/documents/interoperability-levels/#sect-5
.. _Linked Data: /linked-data
.. _RDF: /rdf-a
.
