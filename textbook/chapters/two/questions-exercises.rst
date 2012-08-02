===================================
Chapter Two Questions and Exercises
===================================

Questions
---------

1. What are the major challenges that libraries and library systems
   face in organizing collection of resources since the first libraries?
   
   
2. Select a historical library collection. 

	1. How was the collection organized?
	
	2. Does the collection still exist?
	
	3. Does the collection's library systems retain organizational
	   or technical artifacts from its earlier history?

Exercises
---------
1. Using JSON with Python

   Download the `cutter-definitions.json`_. These definitions are from Charles 
   Cutter's `Rules for a Dictionary Catalog`_ [#]_. Using `Python`_'s interactive
   shell, run the following commands from the same directory where you downloaded
   the json file:

   >>> import json
   >>> cutter_defintions = json.load(open('cutter-definitions.json'))

   If you are successful, you should now have a `Python`_ dictionary of Cutter's. Try
   running the following:

   >>> cutter_definitions.keys()
   >>> cutter_definitions.values()
   >>> cutter_definitions["Bracket"]
   >>> cutter_definitions["Title"]
   
2. Answer the following questions

   1. What did you see when your ran the four commands? 
  
   2. How many terms are defined in `cutter-definitions.json`_? 
     (HINT: **len** is your friend)
	
   3. Why is the definition for **Bracket** different from the definition for **Title**?
   
3. Create a JSON Libraries File

   Create a text `JSON`_ file containing a list of arrays for each of the libraries
   mentioned in this chapter.(HINT: Use `Python`_'s json module)
   
   Requirements for each JSON Associative Array
   Each library hash in the JSON should contain key-values for the following:
   
   * Library's name
   
   * Library's founding
   
   * Library URL if it exists
   
4. Python Script for JSON processing

   Create a python script that reads your JSON of the chapter's libraries, 
   then prints the name and URL sorted alphabetically by the library's
   name.
   
5. Add your work to GIT

   Add your JSON Libraries file from step 3, the python script from step 4, 
   and your completed questions to your git branch. Push your changes to 
   the class repository.

.. _cutter-definitions.json: http://www.NEEDURL.com/ 
.. _JSON: http://www.json.org/
.. _Python: http://www.python.org/
.. _Rules for a Dictionary Catalog: http://books.google.com/books?id=2rQYAAAAMAAJ 
