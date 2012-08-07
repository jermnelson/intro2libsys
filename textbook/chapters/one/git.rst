======================================
Git Distributed Version Control System
======================================
All class code and response questions will be managed through the 
distributed version control system called `Git`_. `Git`_ is open source 
and is available on most operating systems. Many open-source projects use
Git to manage their source code for their project; including many of library
open source projects. 

Introduction to Distributed Version Control System (DVCS)
---------------------------------------------------------
Version control is just the ability to keep track of the edit history of
a file or project. Centralized version control systems like `Subversion`_ (`SVN`_)
and Microsoft's `Visual SourceSafe`_ require a master repository hosted on a dedicated
server that keeps a master copy. Developers check-out code from the master, make changes,
and then commit those changes back to the central repository. Other developers can 
then check-out the code changes from the central repository and continue working on the 
code-base. The advantages of having a centralized version control system is that there is
a canonical or master copy of the code-base that can be used for reference by all of the
project members. While a centralized source code system works well for a traditional 
hierarchical organizations with clearly delineated responsibilities and good coordination 
and communication between members of the project or team, this model of software code 
versioning doesn't very work well for less structured open source projects where members 
are geographically dispersed without clear lines of responsibilities. 

Problems with a centralized approach becoming quickly apparent when individual 
developers check-out the same code but make incompatible changes that then require 
explict resolutions of the conflicts  in order to 
successfully commit the changes back to the master. Also, with a master repository,
corruption in the master or central repository is usually catastropshic. 

The critical feature of a DVCS is the absence of a central, master copy of the 
code-base. Instead, each developer maintains a copy of the code base where local
changes are committed and tracked. Other developers can pull changes into their 
own repository with merging between the different versions done automatically and
any conflicts being flagged for attention by the developer. Often, a central repository 
is designated as a "central" server only in that all branches are merged to a single
branch. In this model, the advantages of a central code-base are maintained (i.e. a 
master copy for reference and download) but still allow for easier tracking and merging
on a distributed code.
 

Popularity of Git
-----------------
Git originally started and was initially developed by Linus Torvalds, the 
creator of the Linux operating system, as a method of managing the code
for the Linux kernal. Torvalds relatively early in the project history turned
control over to other developers to manage and Git has increased quickly in
usage ever since.

While there hasn't been a formal survey of what is the most popular revision control system,
the open-source project comparision website `Ohloh`_ tracks the choice of repository software
with the following breakdown [#]_ :

+------------+-----+
| Subversion | 54% |
+------------+-----+
|        Git | 27% |
+------------+-----+
|        CVS | 12% |
+------------+-----+
|  Mercurial |  2% |
+------------+-----+
|     Bazaar |  2% |
+------------+-----+   

While these numbers are biased because commerical and proprietary software projects are not
being tracked on `Ohloh`_ they do show that even with the advantages mentioned above for DVCS,
the centralized open-source projects `Subversion`_ and CVS still make up over of 66% of projects 
but this percentage has been decreasing over time as Git and other DVCS gain in popularity. 

A number of tutorials are available on `Git`_ including `Git Magic`_ and `Pro Git`_. 

Github
------
Github is a widely used and popular resource for hosting primarily open-source 
Git repositories.

Library Open Source Projects using Git & Github
-----------------------------------------------
The number of library open source projects using Git is large and growing.  Here is a partial list of 
projects with a library focus:

  * Aristotle Library Apps
  * Blacklight
  * Islandora
  * pyMARC
  * VuFind
  

References
----------
.. [#] `http://www.ohloh.net/repositories/compare <http://www.ohloh.net/repositories/compare>`_ , 
       accessed on August 6, 2012.
.. [#] Lynn, Ben `Git Magic`_, accessed on August 6, 2012

.. _Git: http://git-scm.com/
.. _Git Magic: http://www-cs-students.stanford.edu/~blynn/
.. _Ohloh: http://www.ohlog.net/
.. _Pro Git: http://git-scm.com/book
.. _Subversion: http://subversion.tigris.org/
.. _SVN: http://subversion.tigris.org/
.. _Visual SourceSafe: http://msdn.microsoft.com/en-us/library/3h0544kx%28VS.80%29.aspx
