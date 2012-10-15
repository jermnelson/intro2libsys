==============================
Intro2LibSys Operations Set-up
==============================

git
---
`Intro2LibSys`_ uses the free and open source distributed version control
systems called `git`_. To install `git`_ on Ubuntu, run the following:

  .. sudo apt-get install git

The publically available source code repository is hosted on github at
`https://github.com/jermnelson/intro2libsys <https://github.com/jermnelson/intro2libsys>`_

make
----
Install make with:

  .. sudo apt-get install make

virtualenv
----------
To get the DSL and Textbook up and running, I recommend using `virtualenv` to 
create an additional level of abstraction for installing `Intro2LibSys`_ and
accompanying textbook. The easiest method I have found to quickly create a 
virtualenv is to download and run the python script at 
`<https://raw.github.com/pypa/virtualenv/master/virtualenv.py>`_.

Create a new virtualenv after downloading the script:

  .. python virtualenv.py {name-of-environment}


Python Modules
--------------
To use the textbook and DSL, you'll need to first activate the python
virtual environment by 

  .. source {name-of-environment}/bin/activate

You should now see the prompt change with the virtualenv environment you
created prefixed in the command prompt.

django
^^^^^^
Install the latest stable version of `Django`_ with the following:

  .. pip install django

sphinx
^^^^^^
Installs the `Sphinx` python documentation generator module for manipulating
all reStructured text in the DSL and textbook. 

.. _Django: https://www.djangoproject.com/
.. _git: http://git-scm.com/
.. _Intro2LibSys: http://www.intro2libsys.info
.. _Sphinx: http://sphinx.pocoo.org/
.. _virtualenv: http://www.virtualenv.org/
