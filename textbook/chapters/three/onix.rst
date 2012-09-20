============================================
Online Information Exchange (ONIX) for Books
============================================
`ONIX`_ is a meta-data standard used by the book publishing industry
for representing product information in an electronic format. `ONIX`_
is implemented in XML and is compose of three standards; Level 1, 
Level 2, and Level 3. Level 3 is the latest ONIX standard and is not
backward compatible with Levels 1 and 2. The Level 3 standard offers
better handling of born-digital and other electronic resources. ONIX
offers two elements sets that represent the same information; the first
uses reference names while the second uses short tags. 

Examples
--------
Here is a excerpt of an ONIX record for Jane Austen's 
**Pride and Prejudice** using reference names::

	<Product>
	  <DescriptiveDetail>
	   <TitleDetail>
		 <TitleType>01</TitleType>
		 <TitleElement>
		   <TitleElementLevel>01</TitleElementLevel>
		   <TitleText>Pride and Prejudice</TitleText>
		 </TitleElement>
	   </TitleDetail>
	   <Contributor>
		 <SequenceNumber>1</SequenceNumber>
		 <ContributorRole>A01</ContributorRole>
		 <NamesBeforeKey>Jane</NamesBeforeKey>
		 <KeyNames>Austen</KeyNames>
	   </Contributor>
	  </DescriptiveDetail>
	<Product>
	
Here is an except of an ONIX record for Jane Austen's 
**Pride and Prejudice** using short tags::

	<product>
	 <descriptivedetail>
	  <titledetail>
		<b202>01</b202>
		<titleelement>
		 <x409>01</x409>
		 <b203>Pride and Prejudice</b203>
		</titleelement>
	  </titledetail>
	  <contributor>
	   <b034>1</b034>
	   <b035>A01</b035>
	   <b039>Jane</b049>
	   <b040>Austen</b040>
	  </contributor>
	 </descriptivedetail>
	</product>
	
.. _ONIX: http://www.bisg.org/what-we-do-21-15-onix-for-books.php   