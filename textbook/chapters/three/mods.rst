=========================================
Metadata Object Description Schema (MODS)
=========================================
The `Metadata Object Description Schema`_ or `MODS`_ is an XML vocabulary for describing
bibliographic records using similar ideas and a simplified format similar to MARC

Pros
----
*. Specification supported by `Library of Congress`_

*. Interoperability with `MARC`_ accomplished through XML crosswalk from `MARCXML`_
   using `XSLT`_ scripts.


Cons
----
*. Not as semanticially rich as `MARC`_, cannot guarenttee a lossless round-trip
   with `MARC`_ i.e. (MARC1->MODS->MARC1, MARC1 != MARC2) 

.. _`Library of Congress`: http://www.loc.gov/
.. _`MARC`: http://www.loc.gov/marc/
.. _`Metadata Object Description Schema`: http://www.loc.gov/standards/mods/
.. _`MODS`: http://www.loc.gov/standards/mods/
