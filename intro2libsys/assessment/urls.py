"""
 `mod`:urls - Learners Django URLS module for Intro2Libsys DSL
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'assessment.views.home', name='Assessment-Home'),
    url(r'^examinations$', 'assessment.views.examinations', name='Assessment-Examinations'),
    url(r'^exercises$', 'assessment.views.exercises', name='Assessment-Exercises'),
    url(r'^final$', 'assessment.views.final', name='Final'),
    url(r'^midterm$', 'assessment.views.midterm', name='Midterm'),
    url(r'^project$', 'assessment.views.project', name='Assessment-Project'),
    url(r'^quizzes$', 'assessment.views.quizzes', name='Assessment-Quizzes'),
    url(r'^quiz$', 'assessment.views.quiz', name='Assessment-Quiz'),
    url(r'^test$', 'assessment.views.examination', name='Assessment-Test'),
    url(r'^library-systems-job-exercise$','assessment.views.job_exercise', name='Assessment-Job-Exercise'),
    url(r'^fail-essay-exercise$','assessment.views.fail_exercise', name='Assessment-Fail-Exercise'),
)
