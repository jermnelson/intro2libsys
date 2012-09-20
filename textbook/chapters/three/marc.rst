==================================
Machine Readable Cataloging (MARC)
==================================
`MARC`_, an acronym for **MA** chine **R** eadable **C** ataloging, is an 
electronic format and carrier for bibliographic records. The MARC21 (the 
latest version of MARC) format has three components:

* As communication format structure for data exchange between different
  systems
 
* As an ISO 2709 data element set with MARC variable and fixed length fields
  and codes
  
* As actual data with encoding of bibliographic and authority records first
  using the general rule sets of AACR2, DAC, and now RDA
  
The general order of fields in a MARC records is the leader, fixed fields, and then 
variable fields. A field is a logical division in the MARC record with a 3-digit
number "tag" that identifies the type and content of field. The leader is the first 
24 characters of the record, with each character position either being a code or 
blank (some character positions are required) for such things as the record length,
status, type of record, encoding, and cataloging information. The leader is primary
used by the computer systems that then is able to display the information in a more
human-friendly format. 

Here is a table from *Understanding MARC* [#]_ of most commonly used fixed and 
variable length fields in a MARC bibliographic record:

+---------+-------------------------------------------------------------------+
| MARC tag| Description                                                       |
+=========+===================================================================+
| 010 tag | marks the Library of Congress Control Number(LCCN)                |
+---------+-------------------------------------------------------------------+
| 020 tag | marks the International Standard Book Number (ISBN)               |
+---------+-------------------------------------------------------------------+
| 100 tag | marks a personal name main entry (author)                         |
+---------+-------------------------------------------------------------------+
| 245 tag | marks the title information (which includes the title, other      |
|         | title information, and the statement of responsibility)           |
+---------+-------------------------------------------------------------------+
| 250 tag | marks the edition                                                 |
+---------+-------------------------------------------------------------------+
| 260 tag | marks the publication information                                 |
+---------+-------------------------------------------------------------------+
| 300 tag | marks the physical description (often referred to as the          |
|         | "collation" when describing books)                                |
+---------+-------------------------------------------------------------------+
| 490 tag | marks the series statement                                        |
+---------+-------------------------------------------------------------------+
| 520 tag | marks the annotation or summary note                              |
+---------+-------------------------------------------------------------------+
| 650 tag | marks a topical subject heading                                   |
+---------+-------------------------------------------------------------------+
| 700 tag | marks a personal name added entry (joint author, editor, or       |
|         | illustrator)                                                      |
+---------+-------------------------------------------------------------------+


For MARC fields greater than 009, they have can up to two field indicators for 
greater specificity of the type and role of the content in the field. Variable 
length fields also have subfields, a way to further break-down the field into more
discrete "chunks" of information. Subfields start with a code, either a letter or
number, and a delimiter.

Below is an example of a MARC record for the 1918 edition of Jane Austen's 
*Pride and Prejudice*::

	LEADER 00000nam  2200289Ia 4500 
	001    8383316 
	003    OCoLC 
	005    19981012112243.0 
	008    820430s1918    nyu           000 1 eng   
	010    18007296 
	040    DLC|cZMM|dZMM 
	049    COCA 
	090    PR4034|b.P7 1918 
	090    PR4034|b.P7 1918 
	100 1  Austen, Jane,|d1775-1817 
	245 10 Pride and prejudice /|cby Jane Austen; with an 
		   introduction by William Dean Howells 
	260    New York, Chicago [etc.] :|bC. Scribner's sons,|c[c1918] 
	300    xxiii, 401 p. ;|c18 cm 
	490 1  The modern student's library 
	500    Series title also at head of t.-p 
	700 1  Howells, William Dean,|d1837-1920 
	830  0 Modern student's library 
	
This is a common display for MARC records that you'll often see in the MARC 
view in a library catalog. A couple things to notice is that the subfield *a* 
is not explictly shown while the subsiquent subfields are with the "|" as a
subfield delimiter. 

.. [#] `Understanding MARC`_, What is a MARC Record and Why is it Important? Part III. MARC
       Terms and Their Definitions.

.. _MARC: http://www.loc.gov/marc/
.. _Understanding MARC: http://www.loc.gov/marc/umb/
