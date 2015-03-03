Date: 2013-03-19
Title: Metadata Object Description Schema (MODS)

Metadata Object Description Schema (MODS)
-----------------------------------------
The [Metadata Object Description Schema](http://www.loc.gov/standards/mods/) or 
MODS is an XML vocabulary for describing bibliographic records using 
similar ideas and a simplified format to 
[MARC21](http://www.loc.gov/marc/) using more descriptive 
names than the MARC tags for element names. There are no required elements
in a MODS record although the record must have at least one element.

Pros
----
* Specification supported by [Library of Congress](http://www.loc.gov/)

* Interoperability with MARC accomplished through XML crosswalk from 
  [MARCXML](http://www.loc.gov/standards/marcxml/)
  using [XSLT](http://www.w3.org/TR/xslt) scripts.


Cons
----
* Not as semanticially rich as [MARC21](http://www.loc.gov/marc), cannot guarenttee a 
  lossless round-trip with MARC21 i.e. (MARC21a->MODS->MARC21b, MARC21a != MARC21b) 
