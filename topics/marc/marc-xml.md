Title: MARCXML

MARCXML
-------
The Library of Congress has also released an XML version of MARC called 
[MARCXML](http://www.loc.gov/standards/marcxml/) that
represents the MARC leader, fixed fields, and variable fields, along with the indicators
and subfields using an XML schema. There are a number of different programs that convert 
MARC21 into MARC XML without losing any data from the original MARC record. MARCXML is 
useful because of the large number of XML software and techniques that exist but the drawback is
that the MARCXML can be larger than the MARC21 record and that it is merely a direct representation
of the MARC21 record into corresponding XML elements and attributes. 

Below is part of the MARCXML from the Jane Austen's Pride and Prejudice:

     <?xml version="1.0" encoding="UTF-8"?>
     <collection xmlns="http://www.loc.gov/MARC21/slim">
     <record>
      <leader>LEADER 00000nam  2200289Ia 4500</leader>
	<controlfield tag="001">8383316</controlfield>
	<controlfield tag="003">OCoLC</controlfield>
	<controlfield tag="005">19981012112243.0</controlfield>
	<controlfield tag="008">820430s1918    nyu           000 1 eng  </controlfield>
	<datafield tag="010" ind1=" " ind2=" ">
         <subfield code="a">18007296</subfield>
        </datafield>
	<datafield tag="040" ind1=" " ind2=" ">
	  <subfield code="a">DLC</subfield>
          <subfield code="c">ZMM</subfield>
         <subfield code="d">ZMM</subfield>
        </datafield>
	 ...
	<datafield tag="100" ind1="1" ind2=" ">
         <subfield code="a">Austen, Jane,</subfield>
         <subfield code="d">1775-1817.</subfield>
        </datafield>
	<datafield tag="245" ind1="1" ind2="0">
         <subfield code="a">Pride and prejudice /</subfield>
         <subfield code="c">by Jane Austen; with an introduction by William Dean Howells</subfield>
        </datafield>
	<datafield tag="700" ind1="1" ind2=" ">
          <subfield code="a">Howells, William Dean,</subfield>
	  <subfield code="d">1837-1920</subfield>
	</datafield>
	<datafield tag="830" ind1=" " ind2="0">
	 <subfield code="a">Modern student's library</subfield>
	</datafield>
      </record>
     </collection>

