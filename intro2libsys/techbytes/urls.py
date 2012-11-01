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
)
