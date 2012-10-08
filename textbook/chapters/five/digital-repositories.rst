====================
Digital Repositories
====================
Institutional Digital Repositories are a class of software for perserving and 
accessing digital content. In 2007-2008, the National Library of Medicine went 
through an exhaustive evaluation process of digitial repository systems described
in their `report`_.

To properly store digital objects requires that the digital repository meet two 
challenges; first, is the physical preservation of the digital object on either a
hard-drive (even if that hard-drive is abstracted in a virtual server) or other
magnetic or optical medium like digital tape or CD-ROM. The second challenge is
making sure that the data is accessability through software means. Often digital
objects become unusable because of a combination of the two; i.e. the digital object
can only be accessed through an obsolete software program and is located on old media
like a floppy disk. The Duraspace Foundation (they are the organization responsible for 
`Fedora Commons`_ and `DSpace`_ digital repository platforms) calls digital objects
"durable" [#]_  if the object can be migrated to new physical medium and is in format that 
will be accessable for time.


Open-Source
-----------
Fedora, Islandora, Hydra, & Eulfedora
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Fedora Commons`_ is the leading and one of most widely adopted institutional repository
software, either commerical or open source, and is describes as thus on their website:

   The Fedora Repository Project (i.e., Fedora) implements the Fedora abstractions in a 
   robust open source software system.  Fedora provides a core repository service (exposed 
   as web-based services with well-defined APIs).   In addition, Fedora provides an array 
   of supporting services and applications including search, OAI-PMH, messaging, administrative 
   clients, and more.  Fedora provides RDF support and the repository software is integrated 
   with semantic triple store technology, including the Mulgara RDF database. Fedora helps ensure 
   that digital content is durable by providing features that support digital preservation. [#]_

`Islandora`_ is a Drupal interface to Fedora and provides the following description: 

   Islandora is an open source framework developed by the University of Prince Edward 
   Island's Robertson Library. Islandora combines the Drupal and Fedora open software 
   applications to create a robust digital asset management system that can be fitted 
   to meet the short and long term collaborative requirements of digital data stewardship. 
   Additional open source applications are added to this core stack to create what we 
   call Solution Packs.  Islandora operates under a GNU license. [#]_
   
`Hydra`_ is a Ruby-on-Rails interface built on `Blacklight`_ and describes itself as:

   Hydra is a repository solution that is being used by institutions on both sides 
   of the North Atlantic to provide access to their digital content.  Hydra provides 
   a versatile and feature-rich environment for end-users and repository administrators 
   alike. [#]_
   
`EULfedora`_ is similar to `Hydra`_ by providing an Python interface to Fedora Commons as
describes the project as:

   EULfedora is an extensible library for creating and managing digital objects in a 
   Fedora Commons repository. It eases mapping Fedora digital object types to Python 
   classes along with ingesting, managing, and searching reposited content. Its builtin 
   datastream abstractions include idiomatic Python access to XML and RDF datastreams. 
   They're also extensible, allowing applications to define other datastream types as needed. [#]_
   
DSpace
^^^^^^
`DSpace`_, as explained on their website:

    DSpace is the software of choice for academic, non-profit, and commercial 
    organizations building open digital repositories.  It is free and easy to install 
    "out of the box" and completely customizable to fit the needs of any organization.

    DSpace preserves and enables easy and open access to all types of digital content
	including text, images, moving images, mpegs and data sets.  And with an ever-growing 
	community of developers, committed  to continuously expanding and improving the software, 
	each DSpace installation benefits from the next. [#]_

BePress - Digital Commons
^^^^^^^^^^^^^^^^^^^^^^^^^
`BePress Digital Commons`_ is a hosted, open source product and is described on 
their website as:

   Digital Commons is a suite of tools and services that enables institutions 
   to manage, display, and publish scholarship to the web in a beautiful, 
   highly visible online showcase. As the leading hosted institutional repository
   (IR) platform, Digital Commons offers all of the features of a traditional IR as 
   well as professional-grade publishing tools and our SelectedWorks tm individual scholar pages.

   With Digital Commons, institutions can collect, preserve, and make visible all of 
   their intellectual output, including pre-prints, working papers, journal articles, 
   dissertations, master's theses, conference proceedings, presentations, data sets, 
   images, and a wide variety of other content types. [#]_


Commercial
----------
The following table is the top commerical digital repository, or as the Automation
report classifies, Digital Library Management Systems, from the same report [#]_ .

+-------------------------+------------+-----------+
|                         | Total 2011 | Total     |
|                         | Contracts  | Installed |
+-------------------------+------------+-----------+
| SirsiDynix's Portfolio  | 44         | 55        |
+-------------------------+------------+-----------+
| Ex Libris Group's       | 12         | 208       |
| DigiTool and Rosetta    |            |           |
+-------------------------+------------+-----------+
| OCLC's CONTENTdm        |            | 924       |
+-------------------------+------------+-----------+

Ex Libris - Digitools & Rosetta 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
`Rosetta`_ and `Digitools`_ are two digital repository product by Ex Libris. 

Here is how Ex Libris describes Rosetta on their website:

    Tasked with preserving cumulative knowledge, libraries and other memory 
	institutions around the world are taking an increasingly proactive approach 
	to the preservation of digital information. To help these institutions 
	fulfill their mission and ensure that scholarship and heritage continue to 
	be accessible now and in the future, Rosetta from Ex Libris provides a highly 
	scalable, secure, and easily managed digital preservation system. [#]_
	
Ex Libris description of Digitools:

    DigiTool&reg; enables academic libraries and library consortia to manage 
	and provide access to digital resources, both those that are created for 
	use within the institution and those that are collected and maintained by 
	the library for the benefit of the public. [#]_

OCLC - CONTENTdm
^^^^^^^^^^^^^^^^
`CONTENTdm`_ is a digital repository service from `OCLC`_ and here is it's onn 
OCLC's website:

    CONTENTdm&reg; makes everything in your digital collections available to everyone, 
	everywhere. No matter the format - local history archives, newspapers, books, maps, 
	slide libraries or audio/video - CONTENTdm can handle the storage, management and 
	delivery of your collections to users across the Web [#]_

OAI-PMH
-------
The `Open Archives Initiative Protocal for Metadata Harvesting`_
(OAI-PMH) is an XML-based technology that provides a base level of digital
repository interoperabilty with library ILS, OPACs, and more recently
discovery layers and library services platforms.


References
----------

.. [#] `http://www.durspace.org/node/1197 <http://www.durspace.org/node/1197>`_
.. [#] `http://www.fedora-commons.org/about <http://www.fedora-commons.org/about>`_ accessed on July 11, 2012.
.. [#] `http://islandora.ca/about <http://islandora.ca/about>`_ accessed on July 11, 2012.
.. [#] `http://hydraproject.org/ <http://hydraproject.org/>`_ accessed on July 11, 2012.
.. [#] `http://eulfedora.readthedocs.org/en/0.19.0/index.html <http://eulfedora.readthedocs.org/en/0.19.0/index.html>`_ accessed on July 11, 2012.
.. [#] `http://www.dspace.org/introducing <http://www.dspace.org/introducing>`_ accessed on July 11, 2012. 
.. [#] `http://digitalcommons.bepress.com/faq/ <http://digitalcommons.bepress.com/faq/>`_ accessed on July 11, 2012.
.. [#] `Automation Marketplace 2012: Agents of Change <www.thedigitalshift.com/2012/03/ils/automation-marketplace-2012-agents-of-change/>`_
.. [#] `http://www.exlibrisgroup.com/category/RosettaOverview <http://www.exlibrisgroup.com/category/RosettaOverview>`_ accessed on July 11, 2012.
.. [#] `http://www.exlibrisgroup.com/category/DigiToolOverview <http://www.exlibrisgroup.com/category/DigiToolOverview>`_ accessed on July 11, 2012
.. [#] `http://www.contentdm.org/ <http://www.contentdm.org/>`_ accessed on July 11, 2012

.. _BePress Digital Commons: http://digitalcommons.bepress.com/
.. _Blacklight: http://projectblacklight.org/
.. _CONTENTdm: http://www.contentdm.org/
.. _DSpace: http://www.dspace.org/introducing 
.. _Digitools: http://www.exlibrisgroup.com/category/DigiToolOverview
.. _EULfedora: http://eulfedora.readthedocs.org/
.. _Fedora Commons: http://www.fedora-commons.org/
.. _Hydra: http://hydraproject.org/
.. _Islandora: http://islandora.ca
.. _OCLC: http://www.oclc.org/
.. _Open Archives Initiative Protocal for Metadata Harvesting: http://www.openarchives.org/pmh/

.. _report: http://www.nlm.nih.gov/digitalrepository/DRESWG-Report.pdf
.. _Rosetta: http://www.exlibrisgroup.com/category/RosettaOverview
