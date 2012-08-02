"""
 `mod`:urls - Background Django URLS module
"""
from django.conf.urls import patterns, include, url
from views import session_switcher
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'intro.views.home', name='Curriculum-home'),
    url(r'^(\d+)$',session_switcher, name='Curriculum-session'),

##    url(r'^(\d+)$','Curriculum.views.session', name='Curriculum-session'),
##    url(r'^(\d+)/slides/(\d+)$','Curriculum.views.slide', name='Curriculum-slide'),
                    
)
