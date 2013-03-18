"""
 `mod`:urls - Topics Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'topics.views.home', name='Topics-Home'),
    url(r'([\w-]+)$', 'topics.views.topic', name='Topics-Detail'),
)
