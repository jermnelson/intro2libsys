==========
Schema.org
==========
In 2011, Google, Microsoft, and Yahoo started a initative to provide a common 
set of HTML tags and attributes, called schemas, that allows websites to 
semantically describe common objects like websites, books, music, and media
for harvesting by these search engines. In November of 2011 Yandex, the largest
search engine in Russia, joined the initative. These schema are available at 
`schema.org`_. 

There was some tension between `schema.org`_ with the already existing efforts 
by the W3C's RDFa project. Similar to RDFa, you can add `schema.org`_ markup 
to existing HTML elements using the `schema.org`_ microdata. `Microdata`_ is
a proposed addition to the HTML5 specification that offers a simplier method
for embedding semantic information into web-pages. The vocabularies at 
`schema.org`_ are all implemented using microdata.

Examples
--------
First, an example of HTML without `schema.org`_ microdata::

  <html>
   <head>
    ...
   </head>
   <body>
    <h1>Pride and Prejudice</h1>
    <div>written by Jane Austen</div>
    ...
   </body>
  </html>

The same HTML with `schema.org`_ microdata::

  <html>
   <head>
    ...
   </head>
   <body itemscope itemtype="http://schema.org/WebPage">
    <div itemscope itemtype="http://schema.org/Book">
     <h1 itemprop="name">Pride and Prejudice</h1>
     <div itemprop="author">written by Jane Austen</div>
    ...
    </div>
   </body>
  </html>

.. _Microdata: http://diveintohtml5.info/extensibility.html
.. _schema.org: http://schema.org/ 
