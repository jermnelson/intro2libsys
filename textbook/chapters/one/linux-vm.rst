====================
Linux Virtual Server
====================
You will be expected to run your course assignments and projects on a 
Linux Virtual Server. The latest `Ubuntu Server release`_ is used for 
development and demonstration of class projects; however, if you are more
comfortable using another Linux distribution, please use what you are
most comfortable with using. 

A Ubuntu Virtual Machine image can also be downloaded and
used in other cloud providers including Microsoft's Azure cloud services 
(a note of irony for those of us who remember Steve Ballmer saying that
Linux was a cancer, maybe he was right!):

  **Steve Ballmer once described Linux as a "cancer", but in recent months 
  we've heard that Microsoft is running its Skype division off Linux boxes, 
  and it's now offering a Linux-based version of its Azure cloud service - 
  does this give you satisfaction?**

  Well, let's say that I'm relieved that Microsoft seems to have at least 
  to some degree stopped seeing Linux as the enemy. The whole "cancer" 
  and "un-American" thing was really pretty embarrassing.

  `Linus Torvalds BBC Interview`_ 13 June 2012


Your Linux VM should be publically available on a registered
a domain name of your choosing. Learning how to manage a cloud-based Linux server
provides you with experience of managing live and active servers on the same
architecture you'll be using as a librarian or employee in a typical small
to mid-range information technology group in libraries or other organizations.

Linux Basics
------------
Linux, as an open-source UNIX-style operating systems, is different from 
Microsoft Windows or Macintosh operating systems. You will learn the 
Linux command-line instead of a Graphical User Interface (GUI) to run the
`Python`_ and `Django`_ programs for technical exercises and your group
project. 

Critical Commands
^^^^^^^^^^^^^^^^^
Here is a table of Linux commands that are critical to navigating and using Linux
from the command-line. You can get always get more information for most commands
by running **man {name of command}** for the command's man (for manual)
page.

+---------+-------------------+-------------------------------+
| Command | Name              | Usage                         |
+---------+-------------------+-------------------------------+
|  *ls*   | list directory    | Used to display a directory's |
|         | contents          | files, subdirectories, and    |
|         |                   | permissions. **ls -ltra**     |
|         |                   | will display all files and    |
|         |                   | directories, including hidden.|
+---------+-------------------+-------------------------------+
| *cd*    | change directory  | Used to change directories,   |
|         |                   | **cd ../** for going up one   |
|         |                   | directory.                    |
+---------+-------------------+-------------------------------+
| *rm*    | remove            | Deletes a file or directory.  |
|         |                   | **rm -rf** will force delete  |
|         |                   | a directory and all of its    |
|         |                   | contents.                     |
+---------+-------------------+-------------------------------+
| *sudo*  | run as super user | Runs any command in           |
|         |                   | super-user or admin mode      |
|         |                   | you need to be in the sudo    |
|         |                   | group.                        |
+---------+-------------------+-------------------------------+
| *mkdir* | make directory    | Creates an empty directory    |
+---------+-------------------+-------------------------------+
| *ps*    | processes         | Displays a list of running    |
|         |                   | processes or programs on the  |
|         |                   | operating programs.           |
+---------+-------------------+-------------------------------+
| *kill*  | kills running     | Used to kill a process,       |
|         | process           | usually by process id (PID)   |
+---------+-------------------+-------------------------------+

Editing Text
^^^^^^^^^^^^
One of the most common tasks you will do in administrating, managing, or
developing on a Linus server is editing text-based configuration, code,
or documentation files. While there is a long-standing geek feud about what 
is the best text editor, the most widely used text editors on Linux are
`VI`_, `Emacs`_, and `Pico`_. While `Pico`_ is easier to use for beginners, 
`VI`_ and `Emacs`_ have advanced features that assist in code development and
writing technical documentation. 

.. _Emacs: http://www.gnu.org/software/emacs/
.. _Linus Torvalds BBC Interview: http://www.bbc.com/news/technology-18419231
.. _Pico: http://www.udel.edu/topics/software/general/editors/unix/pico/
.. _Ubuntu Server release: http://www.ubuntu.com/download/servera
.. _VI: http://www.vim.org/
