"""
 `mod`:urls - Textbook Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^$', 'textbook.views.home', name="Textbook-Home"),
  url(r'^chapter/(?P<number>\d+)$', 'textbook.views.chapter', name="Textbook-Chapter"),
  url(r'^page$', 'textbook.views.page', name="Textbook-page"),

)
