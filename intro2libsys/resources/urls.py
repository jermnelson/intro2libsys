"""
 `mod`:urls - Resources Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'resources.views.home', name='Resources-Home'),
    url(r'([\w-]+)$', 'resources.views.detail', name='Resource-Detail'),
)
