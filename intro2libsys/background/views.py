"""
 `mod`: Background Views
"""
from django.shortcuts import render_to_response
from django.template import RequestContext
import intro.settings as settings
from Curriculum.models import CourseSession
import datetime

sessions = CourseSession.objects.all()
today = datetime.datetime.today()

def assessments(request):
    """
    View assessments background

    :param request: Request
    """
    return render_to_response('assessments.html',
                              {'instructor':settings.INSTRUCTOR,
                               'sessions':sessions,
                               'timestamp':today},
                               context_instance=RequestContext(request))


def home(request):
    """
    Default view for home
    """
    return render_to_response('background.html',
                              {'instructor':settings.INSTRUCTOR,
                               'page':{'name':'background'},
                               'timestamp':today},
                              context_instance=RequestContext(request))


def instructor(request):
    """
    Default view for instructor page, includes contact, CV, and other
    links.

    :param request: Request
    """
    return render_to_response('instructor.html',
                              {'instructor':settings.INSTRUCTOR,
                               'page':{'name':'instructor'},
                               'sessions':sessions,
                               'timestamp':today},
                              context_instance=RequestContext(request))

def prerequisites(request):
    """
    View for prerequisites 

    :param request: Request
    """
    return render_to_response('prerequisites.html',
                              {'instructor':settings.INSTRUCTOR,
                               'page':{'name':'prerequisites'},
                               'sessions':sessions,
                               'timestamp':today},
                              context_instance=RequestContext(request))

def syllabus(request):
    """
    View for course syllabus

    :param request: Request
    """
    return render_to_response('syllabus.html',
                               {'instructor':settings.INSTRUCTOR,
                                'page':{'name':'syllabus'},
                                'sessions':sessions,
                                'timestamp':today},
                                context_instance=RequestContext(request))
  
