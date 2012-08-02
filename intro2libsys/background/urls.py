"""
 `mod`:urls - Background Django URLS module
"""
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'background.views.home', name='background-home'),
    url(r'^[i|I]nstructor$', 'background.views.instructor', name='background-instructor'),
    url(r'^[p|P]rerequisites$','background.views.prerequisites', name='background-prerequisites'),
    url(r'^[a|A]ssessments$','background.views.assessments', name='background-assessments'),
    url(r'^[s|S]yllabus$','background.views.syllabus', name='background-syllabus'),

)
