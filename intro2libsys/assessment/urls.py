"""
 `mod`:urls - Learners Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'assessment.views.home', name='Assessment-Home'),
    url(r'^quiz$', 'assessment.views.quiz', name='Assessment-Quiz'),
    url(r'^test$', 'assessment.views.test', name='Assessment-Test'),
)
