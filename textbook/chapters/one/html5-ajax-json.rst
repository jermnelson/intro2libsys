=======================
HTML5, AJAX, CSS & JSON
=======================
You are expected to be at least familiar with `HTML5`_,
`CSS`_, and `JSON`_. We will be using these technologies for our
assignments and exercises as we progress through this textbooks.


HTML5
-----
HTML5 is an update to the Hypertext Markup Language specification from the 
`World Wide Web Consortium`_ or (W3C). While different browsers have varied support
for different portions of the HTML5 specification, this is changing as the various
organizations and corporations update and release newer versions of their web browsers.

An important consideration when looking at what features to support, is that many 
libraries, due to either policy, support or other considerations, do not support the latest 
web browsers and therefore may not support HTML5. This was more of a problem during the
mid-2000s when Microsoft's `Internet Explorer`_ 6.0 was not updated by Microsoft and many
large corporations and universities standardized on IE 6 and would not permit other 
browsers to be used in the enterprise. As this blog posting notes [#]_ Smashing Magazine's 

As competition increased in the Web Browsers, driven first by the Mozilla foundation's
`Firefox`_ web and later by Apple's `Safari`_ and Google's `Chrome`_ browsers, Microsoft updated
their web browser to better support HTML5 and CSS. Following Apple decision to restrict the
use of Adobe Flash on the iPhone and iPad, more organizations shifted develop from Flash-based
websites to the use of HTML5.

CSS
---
Cascading Style Sheets, currently in its third version, is an auxiliary to HTML that is 
used for styling web pages by specifying the fonts, colors, position, and other aspects of
the structure of the web pages. Through the use of external stylesheets, complex and large
websites can standardize the appearance through common CSS classes and attributes.  

While the ideal is separating the appearance from the structure in a website, by CSS and
HTML, often this best practice is violated because of limitations supporting multiple web 
browsers. An additional wrinkle is that web browsers vary in the supporting the latest 
version of CSS, especially CSS 3. One technique is using web queries in CSS to serve different
variants of CSS to the web browser based on the version or type of device accessing the 
resource.  

Javascript, AJAX, & JSON 
------------------------
The dominate method of providing client-side interaction on web sites is through the 
programming language Javascript. While Javascript has been supported since the late 1990s,
Javascript experienced a renaissance during the lead-up and adoption of the Web 2.0 suite
of techniques, services, and websites in the mid 2000s. The technique of interactive web
services took off and supported by Web 2.0 was using `AJAX`_, or asynchronous javascript with
XML. 

In traditional web development, any server-side interaction requires a full request from
the web server which then returns the complete web page back to the calling web client. In
AJAX, a client web page sends smaller requests to the server and the server can return either
XML or more often JSON. JSON, or Javascript Object Notation, is a subset of Javascript for
representing primitive data structures like lists, associative arrays, and variables. JSON
is easy to use and is widely supported in many different programming and web frameworks. 
JSON is often easier to use and a better match for the type of data exchange between 
heterogeneous web environments that most web sites that use multiple data sources and
services.

References
----------

.. [#] Lazaris, L. `Old Browsers`_

.. _AJAX: http://en.wikipedia.org/wiki/Ajax_%28programming%29
.. _Chrome: https://www.google.com/intl/en/chrome/browser/
.. _CSS: http://www.w3.org/Style/CSS/Overview.en.html
.. _Firefox: http://www.mozilla.org/en-US/firefox/fx/
.. _Internet Explorer: http://windows.microsoft.com/en-us/internet-explorer/products/ie/home/
.. _JSON: http://www.json.org/
.. _HTML5: http://www.w3.org/TR/html5/
.. _Safari: http://www.apple.com/safari/
.. _World Wide Web Consortium: http://www.w3.org/
