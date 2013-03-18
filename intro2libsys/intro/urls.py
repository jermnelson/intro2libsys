"""
 `mod`:urls - Introduction to Library Systems Django URLS module
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'intro.views.home', name='home'),
    url(r'^about$', 'intro.views.about', name='about'),
    url(r'^(\d{4})/$','syllabus.views.year'),
    url(r'^(\d{4})/(\d{2})/$','syllabus.views.month'),
    url(r'^(\d{4})/(\d{2})/(\d+)/$','syllabus.views.session'),
#    url(r'^background/', include('background.urls')),
#    url(r'^sessions/', include('Curriculum.urls')),
    url(r'^assessment/',include('assessment.urls')),
    url(r'^learner/',include('learners.urls')),
    url(r'^syllabus/', include('syllabus.urls')),
    url(r'^techbytes/', include('techbytes.urls')),
    url(r'^textbook/', include('textbook.urls')),
    url(r'^topics/', include('topics.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
