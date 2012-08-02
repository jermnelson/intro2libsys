"""
 `mod`:urls - Introduction to Library Systems Django URLS module
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'intro.views.home', name='home'),
#    url(r'^background/', include('background.urls')),
#    url(r'^sessions/', include('Curriculum.urls')),
    url(r'^syllabus/', 'syllabus.views.home', name='syllabus'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
