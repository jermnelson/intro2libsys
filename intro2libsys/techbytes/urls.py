"""
 `mod`:urls - TechBytes Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'techbytes.views.home', name='TechBytes-Home'),
  url(r'^org-map.html$', 'techbytes.views.orgmap', name='TechBytes-Organizational-Map'),
  url(r'^lean-startup.html$', 'techbytes.views.leanstartup', name='TechBytes-Lean-Startup'),
  url(r'^frbr-rda-marcr.html$', 'techbytes.views.frbr_rda_marcr', name='TechBytes-FRBR-RDA-MARCR'),
  url(r'^cc-marcr-ds-lib-apps.html','techbytes.views.cc_marcr_apps', name="TechBytes-CC-MARCR-Datastore-Library-Apps"),
  url(r'^consortium-marcr-datastore-hybrid-cloud.html','techbytes.views.consortium_marcr_ds_hybrid_cloud', name="TechBytes-Consortium-MARCR-Datastore-Hybrid-Cloud"),
# Addendum views
  url(r'^glossary.html','techbytes.views.glossary', name="TechBytes-Glossary"),
  url(r'^resources.html','techbytes.views.resources', name="TechBytes-Resources"),
  url(r'^task-summary.html','techbytes.views.task_summary', name="TechBytes-Task-Summary"),
  url(r'^manager-summary.html','techbytes.views.manager_summary', name="TechBytes-Manager-Summary"),
  url(r'^leader-summary.html','techbytes.views.leader_summary', name="TechBytes-Leader-Summary"),                
)
