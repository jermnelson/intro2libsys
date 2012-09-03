"""
 :mod:`views` Module for Assessment views in Intro2Libsys DLS.
"""
__author__ = "Jeremy Nelson"

from django.shortcuts import render_to_response
from models import Question,Test
from django.template import RequestContext

def home(request):
    """
    Displays the home page for the Assessment module.

    :param request: HTTP request
    """
    return render_to_response('assessment.html',
                              {},
                              context_instance=RequestContext(request))


def quiz(request):
    """
    Displays a full quiz if user is logged in to DLS; otherwise
    just display the public example views.

    :param request: HTTP request
    """
    if request.REQUEST.has_key('id'):
        pk = request.REQUEST['id']
    elif request.REQUEST.has_key('pk'):
        pk = request.REQUEST["pk"]
    quiz = Quiz.objects.get(pk=pk)
    if request.user.is_authenticated() == True:
        questions = Questions.objects.filter(test=quiz)
    else:
        questions = Questions.objects.filter(test=quiz).filter(is_public=True)
    return render_to_response(request,
                              'assessment-quiz.html',
                              {'quiz':quiz},
                              context_instance=RequestContext(request))

def examination(request):
    """
    Displays a full test if user is logged in to DLS; otherwise
    just display an error page.

    :param request: HTTP request
    """
    return render_to_response(request,
                              'assessment-test.html',
                              {},
                              context_instance=RequestContext(request))


