"""
 `mod`:urls - Learners Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'learners.views.profile', name='Learner-profile'),
    url(r'login$','learners.views.login_view', name='Learner-login'),
    url(r'logout$','learners.views.logout_view', name='Learner-logout'),
    url(r'update$','learners.views.update', name='Learner-update'),
)
