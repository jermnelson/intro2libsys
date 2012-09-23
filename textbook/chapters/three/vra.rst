=================================
Visual Resource Access (VRA) Core
=================================
The `VRA Core`_ is a meta-data standard for describing visual culture works 
along with analog and digital images accompanying the work. `VRA Core`_ is 
a descriptive XML vocabulary with its own element and attributes. `VRA Core`_
includes some administrative and technical metadata elements including 
a rights and relationship information about the visual objects or digital
image surriogates.

`VRA Core`_ has two base elements; a Work element and an Image element. The
Work element records information about the visual item itself like title, the
artist or other entity responsible for creating the work, artistic medium,
and subjects associated with the work. The Image element is for describing 
the digital file along with rights assoicated with that image, of the work. 

Example
-------
Here is an example of a painting described with `VRA Core`_  from 
the Visual Resource Association's website. [#]_ ::

  <vra xsi:schemaLocation="http://www.vraweb.org/vracore4.htm http://www.vraweb.org/projects/vracore4/vra-4.0-restricted.xsd">
   <work id="w_26" source="Core 4 Sample Database (VCat)" refid="26">
    <agentSet>
     <display>Jasper Francis Cropsey (American painter, 1823-1900)</display>
     <notes/>
     <agent>
       <name vocab="ULAN" refid="500012491" type="personal">Cropsey, Jasper Francis</name>
       <dates type="life">
        <earliestDate>1823</earliestDate>
        <latestDate>1900</latestDate>
       </dates>
       <culture>American</culture><role>painter</role>
     </agent>
    </agentSet>
    ...
  </work>
  <image id="i_129" href="http://aal.ucsd.edu/vracore4/example26.html" 
   refid="129" source="VRA Data Standards Committee, Core 4 Sample Records">
   <measurementsSet>
     <display>18 MB</display>
     <notes/>
     <measurements/>
   </measurementsSet>
   <relationSet>
    <relation type="imageOf" refid="26" source="Core 4 Sample Database (VCat)"/>   </relationSet>
   <rightsSet>
    <display>publicDomain</display>
    <rights/>
   </rightsSet>
   ...
  </image>
  </vra>

References
----------
.. [#] `VRA Core 4 Example 26: Landscape painting`_  

.. _VRA Core: http://www.vraweb.org/projects/vracore4
.. _VRA Core 4 Example 26: Landscape painting: http://www.vraweb.org/projects/vracore4/example026.html
