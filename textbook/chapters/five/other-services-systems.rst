==================================
Other Services and Library Systems
==================================

Supporting Technology
---------------------
Authentication
^^^^^^^^^^^^^^
As preimum electronic resource consume a larger portion of academic 
libraries budget, and to a lesser extent, public libraries, coupled with 
the demand of remote access to those preimum resources from off-site, 
requires libraries to provides the means and methods for patron's to 
authenticate their identity to use the resource. Some ILS systems provide
remote authentication through such technologies as reverse proxy, i.e. 
after a user is authenticated, network traffic is rerouted through the 
institution, so that it appears to the vendor that the user is coming through
the institution's IP addresses. This is solution is the bases for a very 
popular solution called `EZProxy`_, a formally open-source project that was purchased
by OCLC and coverted into a paid, commerical service. 

.. sidebar:: Authentication verses Authorization
   :class alert alert-warning
   
   It is easy to conflate authentication with authorization but
   these are two distinct but related concepts. Authentication is the 
   process by which a system determines the identity of a user, usually
   through a secured password and/or encrypted key. Authorization is the
   process by which rights to certain resources and activities are assigned
   and associated to a user. Note that it is not a requirement that the
   user be authenticated as a very common authorization nide is determining what
   rights an anomoymous user has over an authenticated user. Things become
   even more confusing because often the same system often handle both 
   tasks. LDAP is in example of such a technology that combines both roles
   into a single system.

Other authentication options include Lightweight Directory Access Protocol 
(LDAP), `Shibboleth`_, and `OpenID`_. LDAP is an Intenet
protocol that offers a distributed hiearchary of users, groups, rights, and other
directory information along with an authentication mechanisim for binding 
a password to a user. Applications with LDAP access can assign different 
levels of access to functionality depending on the user's role or group
membership. Most often LDAP servers are restricted to a single instituion 
making it difficult or impossible for users to use the same authentication
creditials between different institutions or external applications. Shibboleth 
is an open-source federated identity technology that offers a single signon
for users who use different resources and services from multiple institutions 
or products. Shibboleth is more common at large academic or governmental
research institutions than in smaller colleges and public libraries. 
OpenID is another federated identity that attempts to provide a single-signon
for individuals on the open web. OpenID is supported by some of the largest
and most active websites including Google, Facebook, Yahoo, and Twitter. 

Resource Management
^^^^^^^^^^^^^^^^^^^

Third-party external services
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Libguides, OpenURL, electronic reference services

.. _EZProxy: http://www.oclc.org/ezproxy/
.. _OpenID: http://openid.net/
.. _Shibboleth: http://shibboleth.net/ 