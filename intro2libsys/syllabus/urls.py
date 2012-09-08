"""
 `mod`:urls - Syllabus Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'syllabus.views.home', name='Syllabus-Home'),
    url(r'^project$', 'syllabus.views.project', name='Syllabus-Project'),
    url(r'^instructor-contact$', 'syllabus.views.instructor', name='Syllabus-Instructor'),
 
)
