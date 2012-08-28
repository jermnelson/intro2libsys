============
FRBR and RDA
============
Functional Requirements Bibliographic Records (FRBR)
----------------------------------------------------
FRBR is an entity-relationship model where entities are the objects of interest
that are defined in a most general way as possible along with the relationships 
between entities. Each entity is defined with a set of attributes or 
characteristics and the relationships or associations with other entities. 

FRBR defines three groups of entities.

First Group FRBR Entities
-------------------------
First Group is made up of the intellectual or artistic products and these 
entities are work, expression, manifestation, and items. These four 
entities are often referred to WEMI.

Work
^^^^
A **Work** is the most abstract of the four WEMI entities. As defined by
the FRBR Final Report - "a distinct intellectual or artistic creation" [#]_ 
A **Work** doesn't actually exist in any physical or electronic form; it is an 
entity that is comprised of common attributes from its different **Expressions**.
For example, different editions, abridgments, revisions, and translations are 
all **Expressions** of the **Work** "Pride and Prejudice" by Jane Austen.

Expression
^^^^^^^^^^
An **Expression** is the second-most abstraction in the WEMI model, and is 
defined as "the intellectual or artistic realization of a work in the form 
alpha-numeric, musical, choreographic notation, sound, image, object, movement,
etc., or any combination of such forms." [#]_ Like a **Work**, an **Expression** 
doesn't actually include such physical attributes as the font or page layout, 
but is the unit used to describe more of the content than the physical or 
electronic **Manifestations**. Continuing the "Pride and Prejudice" example, a 
first edition, a film adaptation, and a television adaptation would all be 
considered **Expressions** of a **Work** but would not be the physical book found in 
the stacks or a film's frame-per-second.

Manifestation
^^^^^^^^^^^^^
A **Manifestation** is the third entity in the WEMI and is defined by the FRBR
Final Report as "the physical embodiment of the an expression of a work". [#]_ 
A **Manifestation** includes most materials, such as monographs, periodicals,
films, music scores and recordings, video, websites, DVDs and BlueRay, and most
electronic resources. Identifing a **Manifestation** is about recording the 
physical characteristics, including the physical form, that collectively make
up the set of attributes associated with the physical or electronic item. 

Going back to the "Pride and Prejudice" example, the 1948 edition from Pantheon,
the 1991 Knopf edition, the electronic html from Project Gutenberg, the mp3
audio from Project Gutenberg, the 1940 VHS Video from Metro-Goldwyn-Mayer, and
the BBC 2001 production DVD video are distinct **Manifestations** that
embody each of these **Expressions** of "Pride and Prejudice". 

Item
^^^^
An **Item** is the most concrete entity in WEMI and refers to the actual physical
or electronic item. As defined by FRBR, an item is "a single exemplar of a 
manifestation". [#]_ In most cases an **Item** is a distinct single unit of a 
resource, for example the physical copy of "Pride and Prejudice" that is on 
the shelf. Most often, the intellectual content and physical form are the same
for both an **Item** and its exemplifying **Manifestation** but variations 
in multiple copies of an **Item** could and do exist; for example the library
may have two copies of the 1940 edition of "Pride and Prejudice" but the 
second copy may be damaged and each copy will have a separate barcode.

Second Group FRBR Entities
--------------------------
Second Group is made up the entities responsible for the creation, production, 
publication, dissemination, or custodianship of the first group of entities. 
FRBR identifies these as either person or corporate body entities.

Third Group FRBR Entities
-------------------------
Third Group are entities that serve as subjects for the WEMI entities and are 
concept, object, event and place.

Resource Description and Access (RDA)
-------------------------------------
RDA is a newer framework for bibliographic cataloging that includes guidelines 
and instructions for describing artifacts and relationships of those artifacts 
with entities like a person, organizations, and concepts. RDA is based on the
FRBR and FRAD (Functional Requirements for Authority Data) specifications as well 
as incorporating various elements from AACR2.

RDA is meant to support end user resource discovery in library systems in 
finding a resource, identifying a specific resource among similar resources, 
selecting a resource, and finally obtaining the resource. Likewise, for 
entities associated with resources, RDA should assist end users in finding 
information on the entity or resources associated with the entity, identifying
the entity from among similar entities, clarifying the relationship between the 
entity and other entities, and understanding why an entity has a certain name, 
title, or form.


References
----------
.. [#] page 16, `Functional Requirements for Bibliographic Record: Final Report`_
.. [#] page 18, `Functional Requirements for Bibliographic Record: Final Report`_
.. [#] page 20, `Functional Requirements for Bibliographic Record: Final Report`_
.. [#] page 23, `Functional Requirements for Bibliographic Record: Final Report`_


.. _`Functional Requirements for Bibliographic Record: Final Report`: http://archive.ifla.org/VII/s13/frbr/frbr.pdf
