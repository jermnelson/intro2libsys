==========================
Agile Software Development
==========================
Agile Software Development is a set of software developmental practices and methodology
based on short, iterative cycles, where the requirements are defined for small areas of 
functionality and the code is developed and tested against the requirements.  

.. figure:: http://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Agile_Software_Development_methodology.svg/389px-Agile_Software_Development_methodology.svg.png
[#]_

Agile organizational principles are useful in improving library systems. The 
`Manifesto for Agile Software Development`_  and is as follows:

  **Individuals and interactions** over processes and tools

  **Working software** over comprehensive documentation

  **Customer collaboration** over contract negotiation

  **Responding to change** over following a plan

Technology is complex and can fail spectacularly or present subtle errors with
bizarre side effects. By being transparent along with adaptable approaches to problems, library
systems unifies with the large purpose and goals of the library. The Agile emphasis on simplicity,
should be a good and quick yardstick for evaluating different options to solve 
technology problems that will occur.

User Stories
------------
Most agile methodologies for projects start with the creation of short and simple
descriptions of what the user is trying to accomplish with the software being 
developed. Ideally, these user stories come from the user themselves, either directly
or through observing or interviewing the user. The user stories are then collected 
and prioritized with time estimates for completion.

Test Driven Development
-----------------------
As the user story is implemented in software, Agile methodolgy encourages the creation
of automated software tests to insure that the requirements from the user story are 
being met. There are a number of different ways to test software, with the most radical
being **Test-Driven Development (TDD)**, a model where the developers write the tests first and
then write software code for the system that passes the tests. A common critisim of TDD is
that developers may write code to just pass the tests and not actual meet the requirements. 
The two most common ways to do software testing and both can be used for TDD are 
**Unit Testing** and **Behavior-driven development (BDD)**

Unit testing
^^^^^^^^^^^^
Unit testing at its most basic, is about creating an automated test that can be run 
againest a specific piece of code to see if the code performs as expected given an
initial set of variables and state of the system. 

Behavior-driven development
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Behavior-driven development, or BDD, is a different method for testing software. With BDD,
a user scenario is crafted in way that the test framework and extract test conditions that
are then tested againest the system. While Unit Testing focuses on testing specific code, a
BDD testing is more usefully for testing how well various sections in the code-base interact
to meet a user need or requirement. 

Fast Iterative Cycles
---------------------
Another key characteristic of Agile software developoment are short bursts of coding activity and
project activity that delivers some functionality back to the end users for feedback. These sprints
are usually no longer than a month, so that the project can respond to changing requirements of
the stakeholders in the project. 

References
----------
.. [#] Wikipedia, `Agile Software Develoment`_

.. _Agile Software Development: http://en.wikipedia.org/wiki/Agile_software_development
.. _Manifesto for Agile Software Development: http://agilemanifesto.org/
