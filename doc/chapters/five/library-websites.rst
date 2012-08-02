================
Library Websites
================
One of the primary responsibilities for most Systems Librarians is maintaining,
developing, or improving their institution's website. Often the librarian
is restricted by library policies, technology, or other constraints that can
be challenging as the website is often the only library services many 
users (in the case of academic or special libraries) will ever use.

The range of technologies used for hosting a library website range widely 
from static HTML pages to full enterprise content management systems (CMS) 
hosted through a off-site vendor or insitituional data center. 


Web servers
-----------
The first important piece of technology for a library website is a
web server. At its most basic, a web server responds to a request from
a web client with either static or dynamic content. 

The term web server can cover both the physical hardware that runs the 
web server software. While this can cause confusion (i.e. the web server's
physical memory was exhaused by an irrient process of the web server),
context is important. For the purpose of this section, by web server,
we will mean the second sense of the term; namely that a web server is
the actually software that runs on a physical or virtual server. 

A `Netcraft`_, an internet services company based in England, does a 
monthly survey of what web server websites all over the internet are using
to host their content. In their June 2012 survey [#]_ of over 697,000,000 
websites, the breakdown of the top web server software is as follows:

+---------------------+-----------------+------------+
| Web Server Software | Number websites | Percentage |
+---------------------+-----------------+------------+
| `Apache`_           | 448,452,703     | 64.33%     |
+---------------------+-----------------+------------+
| `Microsoft IIS`_    |  95,891,537     | 13.76%     |
+---------------------+-----------------+------------+
| `nginx`_            |  72,881,755     | 10.46%     |
+---------------------+-----------------+------------+
| `Google`_           |  22,464,345     |  3.22%     |
+---------------------+-----------------+------------+

Other web servers, including custom built web servers by such companies
like Facebook, make up the remaining 8.33% of web servers. By far,
the most popular web server is the open-source `Apache`_ server which 
runs on multiple operating systems, including Windows, Macintosh,
Linux, and BSD flavors. The second most popular web server is Microsoft's
IIS server which is only available on the Windows platform and is not 
open source. The third most popular web server is `nginx`_, a fairly
recent open source web server. 

.. sidebar:: nginx
   :class: alert alert-info
   
   In the past year, I recently switch from using `Apache`_ to 
   `nginx`_ as we publically released Aristotle and the Colorado College
   new Discovery Layer and App portfolio. The power of `Apache`_ is in 
   its user community and in large number of configuration options and 
   plugins available for various types of services. The flip side of 
   `Apache`_ power and flexibility is that complexity of correctly 
   configuring for your needs. 
   
   Having used `Apache`_ for a number of years, I was still very much a 
   newbie configurating and running `Apache`_ that I was nervious by 
   rolling out production instances of these new servers and getting 
   everything to work correctly in the stack of software for the library.
   When I started investigating alternatives, the simplicity, stability,
   and the large websites using it, all favored `nginx`_.
   
   As we moved forwarded at the library, `nginx`_ has proved to be as
   flexible, if not more, than `Apache`_ at being simple to use and 
   easy to configure to serve dynamic content from `Django`_ and
   static files from the file system.
   

Dynamic Web sites & Application servers
---------------------------------------
Most library websites have moved beyond just hosting static web pages 
with images and now have a large number of dynamic elements that generated
when a user visits the website. These dynamic elements, including such things
as a library's hours, events, news, and online chat services, can be part of
the website or increasely are feeds from external systems both within and
outside the library. As libraries have added more social elements, including
Twitter feeds, Facebook comments and widgets, and other services, the complexity
of the website increases and requires more knowledge and expertise of the librarian
charged with maintaining the website. 

The first technology to provide dyanmic element to a library's website are 
CGI (common gateway interface) scripts that process submitted content from the
user. While use of CGI scripts has declined as more library websites shift to 
using Content Management Systems and applications servers, their use for simple
services like email reference services still persist and may require support 
and management from the librarian.

Firewalls
---------


Proxies
-------


OpenURL
--------


Content Management Systems (CMS)
--------------------------------

References
----------
.. [#] `June 2012 Web Server Survey`_


.. _June 2012 Web Server Survey: http://news.netcraft.com/archives/2012/06/06/june-2012-web-server-survey.htm
