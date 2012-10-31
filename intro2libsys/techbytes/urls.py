"""
 `mod`:urls - TechBytes Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'techbytes.views.home', name='TechBytes-Home'),
)
