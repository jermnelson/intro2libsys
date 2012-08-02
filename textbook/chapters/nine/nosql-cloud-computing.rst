=======================
NoSQL & Cloud Computing
=======================
NoSQL is a general term for the class of newer data storage technologies 
that sidestep traditional normalized relational databases that use SQL 
and schemas. This is a very broad category and includes different
types of technology to meet some very different requirements ranging from
key-value datastores like `Redis`_, to Bigtable inspired projects like 
`Hadoop`_ and Facebook's `Cassandra`_, to document-oriented datastores like 
`MongoDB`_, `CouchDB`_ and Amazon's `SimpleDB`_. 

It is not a cocidenence that the development and growth of NoSQL has
coincided with the rise of cloud computing. Some of these technologies are
only available on corporate computing clouds like Amazon's SimpleDB. A very
broad definition of cloud computing is the move towards a delivery of computing
services and data storage on usually external platforms outside the library.
Cloud computing is usually broken down into three area; Software as a Service (SaaS),
Platform as a Service (Paas), and Infrastructure as a Service (IaaS). 

Usually the simplest to get up and running, SaaS shifts the burden of managing servers and
software to a vendor who just provides a remote software stack accessable through
a web browser or lightweight client like a web-browser or native mobile app. 

PaaS is a different model where the cloud vendor provides the computing platform with development and
administrative tools for users to develop their own applications that are then 
accessable and hosted on the vendor's cloud infrastructure. 

The last category of cloud computing, IaaS, is when the cloud vendor hosts 
Virtual Machines (VM) that the client then installs an operating systems 
on the VM. Usually the client, not the cloud vendor, is responsible for 
maintaining and managing the the VM and offers the most flexiblity and power
for creating custom applications for meetings the sometimes complex requirements
of enterprise software. 


References
----------

.. _Cassandra: http://cassandra.apache.org/
.. _CouchDB: http://couchdb.apache.org/
.. _Hadoop: http://hadoop.apache.org/
.. _MongoDB: http://www.mongodb.org/
.. _Redis: http://redis.io/
.. _SimpleDB: http://aws.amazon.com/simpledb/
