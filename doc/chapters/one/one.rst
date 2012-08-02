===============================
Introduction to Library Systems
===============================
The Meaning of "Library Systems"
--------------------------------
Before we can deconstruct the term "Library Systems", we must first 
establish what we mean by the term "library". In order not to be caught-up
in semantic parsing of "library" (although such a discussion is important),
we'll use Wikipedia's definition:
 
   A **library** is an organized collection of books, other other printed 
   materials, and in some cases special materials such as manuscripts, 
   films and other sources of information.
   
   `http://en.wikipedia.org/wiki/Library <http://en.wikipedia.org/wiki/Library>`_

While I think Wikipedia's definition of the types of material to be too 
restrictive and inaccurate, more importantly the definition's key phrase
is at the beginning, "an organized collection". A library must be organized.

So what are "Library Systems" then? Library Systems are how we organize
a library otherwise it is just a random collection of stuff. Along with 
most professions, librarians increasingly depend on their technology to
manage and organization their collections for the benefit of their
users. These collections are more diverse and require sometimes sophisticated 
systems.

.. image:: knox-college-seymour-library-redrum.jpg
   :class: intro

This textbook provides an overview of the typical types of systems a librarian
or other library staff will likely encounter in a public, academic, special, or
corporate library. Having an understanding of the basic structure of typical 
bibliographic records and being able to manipulate theses bibliographic records
are valuable skills as libraries look to expand the usability of their valuable
resources and collections. 

Our emphasis is an overview of the technology used in typical 
public or academic library. First, though, we need to understand some of the
bibliographic theory behind the usually most complex technology in a library
system, the bibliographic catalog. A portion of the exercises in the book will
give you practical experience in library systems development and administration, 
building from some simple to more complex programming and management tasks on 
a number of different open-source technologies. 

These include more general IT systems such as web-servers,
content management systems, and relational databases like Oracle or MySQL.
There are also specific library systems like Integrated Library Systems and
Discovery Layers, Open URL resolvers, electronic resource management systems,
and circulation systems. The middle section will be be an overview of the 
some of the typical technology that library systems are expected to support,
followed by introduction to the larger library technology ecosystem including
vendors, publishers, and library consortiums. Finally, we'll review new 
newer technology that library systems need to adapted to or prepare for,
such as NoSQL data storage, the Semantic web, and mobile platforms, ending
up with a discussion of library systems in a number of futures scenarios. 


.. sidebar:: Libraries & DevOps
   :class: alert alert-info

   `DevOps`_, a combination of Development and Operations, is a newer
   model for managing and administrating a Information Technology department
   in non-technological organizations. `DevOps`_ comes out of the corporate
   world when recognition...
 

   Libraries of all types are under increasing pressure to provide
   resources on multiple platforms to multiple user groups with static, or
   worse, declining budgets. What are the current practices in library
   systems groups? How might a DevOps model help address this challenge?

Structure of this Textbook
--------------------------
This book will primarily focus on the software-side of library systems but
with the recognition that library systems are often also responsible for more
of the server, PC, peripherals, and network hardware in their libraries. What was once a 
separate domains in IT (application development/support and hardware/server
administration) are becoming blurred as cloud and third-party hosting services
are increasingly embedded within the resources and services supported and 
provided by library system groups. We will combining theoretical examination
of the library systems, coupled with software development and systems 
administration exercises using the `Python`_ programming language and, 
other tools. 


Technology used in this Textbook
--------------------------------
Before we begin, you should be familiar with creating a basic website using `HTML`_ and `CSS`_. 
As we progress through the course, you will be exposed and learn about additional technologies
including using the `SQLite`_ database, and the `Redis`_ NoSQL datastore along with `Python`_ and
the `Django`_ webframework. 


.. toctree::
   :maxdepth: 2
   
   git
   linux-vm
   html5-ajax-json
   python-django-restructuredtxt
   project-status
   questions-exercises
   ../appendices/example-course-project



     

.. _The British Museum's Ashurbanipal Library Project: /resources/articles/british-museum-ashurbanipal-library-project
.. _CSS: http://en.wikipedia.org/wiki/Cascading_Style_Sheets
.. _DevOps: http://www.readwriteweb.com/enterprise/2011/08/devops-what-it-is-why-it-exist.php
.. _Django: https://www.djangoproject.com/
.. _Ebla: The World's Oldest Library: /resources/articles/ebla-worlds-oldest-library
.. _Hidden Wisdom and Unseen Treasure: Revisiting Cataloging in Medieval Libraries: /resources/articles/hidden-wisdom-unseen-teasures
.. _HTML: http://en.wikipedia.org/wiki/HTML
.. _Growth and development of Islamic Libraries: /resources/articles/growth-development-islamic-libraries
.. _The intellectual interests reflected in libraries of the fourteenth and fifteenth centuries: /resources/articles/intellectual-interests-reflected-in-libraries
.. _The Library An Illustrated History: /resources/books/library-an-illustrated-history
.. _Mosques as Libraries in Islamic Civilization 700-1400 A.D.: /resourcs/articles/mosques-as-libraries-in-islamic-civilization
.. _Python: http://www.python.org/
.. _Redis: http://redis.io/
.. _SQLite: http://www.sqlite.org/
.. _virtualenv: http://pypi.python.org/pypi/virtualenv
