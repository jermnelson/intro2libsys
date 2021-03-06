Title: What is GIT?

All class code and response questions will be managed through the 
distributed version control system called [Git](http://git-scm.com/). Git is 
open source and is available on most operating systems. Many open-source 
projects use Git to manage their source code for their project; including 
many library open source projects. 

Introduction to Distributed Version Control System (DVCS)
---------------------------------------------------------
Version control is just the ability to keep track of the edit history of
a file or project. Centralized version control systems like 
[Subversion](http://subversion.tigris.org/) (SVN) and Microsoft's 
[Visual SourceSafe](http://msdn.microsoft.com/en-us/library/3h0544kx%28VS.80%29.aspx) 
require a master repository hosted on a dedicated server that keeps a master copy. 
Developers check-out code from the master, make changes, and then commit those changes 
back to the central repository. Other developers can 
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
explicit resolutions of the conflicts  in order to 
successfully commit the changes back to the master. Also, with a master repository,
corruption in the master or central repository is usually catastrophic. 

The critical feature of a DVCS is the absence of a central, master copy of the 
code-base. Instead, each developer maintains a copy of the code base where local
changes are committed and tracked. Other developers can pull changes into their 
own repository with merging between the different versions done automatically and
any conflicts being flagged for attention by the developer. Often, a central repository 
is designated as a "central" server only in that all branches are merged to a single
branch. In this model, the advantages of a central code-base are maintained (i.e. a 
master copy for reference and download) but still allow for easier tracking and merging
on distributed code.
 

Popularity of Git
-----------------
Git originally started and was initially developed by Linus Torvalds, the 
creator of the Linux operating system, as a method of managing the code
for the Linux kernel. Torvalds relatively early in the project history turned
control over to other developers to manage and Git has increased quickly in
usage ever since.

While there hasn't been a formal survey of what is the most popular revision control system,
the open-source project comparison website [Ohloh](http://www.ohloh.net/) tracks the 
choice of repository software with the following breakdown 
<sup><a href="#1">1</a></sup>:

<table class="table">
 <tr>
  <th>Repository</th>
  <th>Percentage</th>
  <th>2012</th>
  <th>2014</th>
  <th>+/-</th>
 </tr>
 <tr>
  <td>Subversion</td>
  <td>54%</td>
  <td>46%</td>
 </tr>
 <tr>
  <td>Git</td>
  <td>27%</td>
  <td>38%</td>
 </tr>
 <tr>
  <td>CVS</td>
  <td>12%</td>
  <td>9%</td>
 </tr>
 <tr>
  <td>Mercurial</td>
  <td>2%</td>
  <td>2%</td>
 </tr>
 <tr>
  <td>Bazaar</td>
  <td>2%</td>
  <td>2%</td>
 </tr>
</table>


While these numbers are biased because commercial and proprietary software projects are not
being tracked on [Ohloh](http://www.ohlog.net/) they do show that even with the advantages 
mentioned above for DVCS, the centralized open-source projects Subversion and CVS still 
make up over of 66% of projects but this percentage has been decreasing over time as Git and 
other DVCS gain in popularity. 

Github
------
[Github](http://www.github.com) is a widely used and popular resource for hosting primarily open-source 
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
  
Git Commands
------------
Here is a list of essential *git* commands

**git init**
   Initializes an empty git repository in a directory. 

**git add {filename-or-directory}**
   Adds the file or all of the contents if a directory to the git repository.

**git status**
   Shows the current status of the git repository including any untracked, new,
   or modified files under source control.
   
**git commit -a -m "{message}"**
   Commits any new and modified files to the repository with a message
   
**git rm {filename-or-directory}**
   Removes the file or directory from the repository. NOTE: this will also 
   delete the file from the file system as well.
   
**git pull origin master**
   Pulls the latest changes from the original parent's master branch. Changed 
   files are either automatically merged by git or an error message will display
   requiring manual resolution of the conflicts.
   
**git push origin master**
   Pushs any changes made and committed on the local clone to the original parent's
   master branch.
   
**git bundle create {name}.bundle master**
  Creates a single binary file of the master branch of the repository suitable 
  for attaching to an email or usb drive. Users can then clone or pull from the
  bundle as any other git repository.
  
**git clone {git-repository file-location or URL}**
  Creates a local, cloned copy of another git repository.
   

References
----------
 <sup><a name="1">1</a></sup> [http://www.ohloh.net/repositories/compare](http://www.ohloh.net/repositories/compare) 
 accessed on August 6, 2012.

 Lynn, Ben `Git Magic`_, accessed on August 6, 2012
