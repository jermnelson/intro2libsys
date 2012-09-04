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

def get_test_questions(request):
    """
    Helper function takes a request and returns a test object and matched all
    questions.

    :param request: HTTP Request
    """
    if request.REQUEST.has_key('id'):
        pk = request.REQUEST['id']
    elif request.REQUEST.has_key('pk'):
        pk = request.REQUEST["pk"]
    test = Test.objects.get(pk=pk)
    if request.user.is_authenticated() == True:
        questions = Question.objects.filter(test=test)
    else:
        questions = Question.objects.filter(test=test).filter(is_public=True)
    return test,questions

def quiz(request):
    """
    Displays a full quiz if user is logged in to DLS; otherwise
    just display the public example views.

    :param request: HTTP request
    """
    quiz,questions = get_test_questions(request)
    return render_to_response('assessment-quiz.html',
                              {'questions':questions,
                               'quiz':quiz},
                              context_instance=RequestContext(request))

def examination(request):
    """
    Displays a full test if user is logged in to DLS; otherwise
    just display an error page.

    :param request: HTTP request
    """
    test,questions = get_test_questions(request)
    return render_to_response('assessment-test.html',
                              {'examination':test,
                               'questions':questions},
                              context_instance=RequestContext(request))


