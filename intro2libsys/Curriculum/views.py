"""
 :mod:`views` Curriculum Views
"""
__author__ = 'Jeremy Nelson'
import os,logging,datetime
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
import intro.settings as settings
from Curriculum.models import *
from django.http import HttpResponse
from django_helpers import BookLoader

sessions = CourseSession.objects.all()
today = datetime.datetime.today()

text_book = BookLoader()

def home(request):
    """
    Displays default Curriculum view
    
    :param request: HTTP Request
    """
    return render_to_response('curriculum.html',
                              {'instructor':settings.INSTRUCTOR,
                               'sessions':sessions,
                               'timestamp':today},
                               context_instance=RequestContext(request))

def session_switcher(request,session_pk):
    if session_pk == "1":
        return session_one(request)
    elif session_pk == "2":
        return session_two(request)

def session_one(request):
    print(text_book.chapters['one'])
    return direct_to_template(request,
                              'session-one.html',
                              {'instructor':settings.INSTRUCTOR,
                               'chapters':[text_book.chapters['one'],
                                           text_book.chapters['two']]})

def session_two(request):

    return direct_to_template(request,
                              'session-two.html',
                              {'instructor':settings.INSTRUCTOR,
                               'chapter':text_book.chapters.get('three')})

def session(request,session_pk):
    """
    Displays individual session
   
    :param request: HTTP Request
    :param session_pk: Session primay key
    """
    session = CourseSession.objects.get(pk=session_pk)
    outcomes = CourseOutcomes.objects.filter(session=session)
    slides = CourseSlides.objects.filter(session=session)
    return render_to_response('session.html',
                              {'instructor':settings.INSTRUCTOR,
                               'outcomes':outcomes,
                               'session':session,
                               'sessions':sessions,
                               'slides':slides,
                               'timestamp':today},
                               context_instance=RequestContext(request))

def slide(request,session_pk,slide_position):
    """
    Displays individual slide for a particular session.

    :param request: HTTP Request
    :param session_pk: Session primary key
    :param slide_position: Slide position
    """
    query = CourseSlides.objects.filter(session=session_pk)\
            .filter(position=int(slide_position))
    if len(query) == 1:
        slide = query[0]
    else:
        slide = None
    return render_to_response(slide.template,
                              {'session':CourseSession.objects.get(pk=session_pk),
                               'sessions':sessions,
                               'slide':slide,
                               'timestamp':today},
                              context_instance=RequestContext(request))
            
    
