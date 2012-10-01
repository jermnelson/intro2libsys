"""
 :mod:`views` Module for Assessment views in Intro2Libsys DLS.
"""
__author__ = "Jeremy Nelson"

from django.shortcuts import render_to_response
from models import Exercise,Question,Test
from django.template import RequestContext

def examination(request):
    """
    Displays a full test if user is logged in to DLS; otherwise
    just display an error page.

    :param request: HTTP request
    """
    test,questions = get_test_questions(request)
    return render_to_response('assessment-test.html',
                              {'examination':test,
                               'questions':questions,
                               'section':'assessment'},
                              context_instance=RequestContext(request))


def examinations(request):
    tests = Test.objects.exclude(category="qz")
    return render_to_response('examinations.html',
                              {'section':'assessment',
                               'tests':tests},
                              context_instance=RequestContext(request))

def exercises(request):
    exercises = Exercise.objects.all()
    return render_to_response('exercises.html',
                              {'exercises':exercises,
                               'section':'assessment'},
                              context_instance=RequestContext(request))

def home(request):
    """
    Displays the home page for the Assessment module.

    :param request: HTTP request
    """
    return render_to_response('assessment.html',
                              {'section':'assessment'},
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

def midterm(request):
    """
    Displays Midterm for print-out or electronic copy. Questions are hard-coded.
    
    :param request: HTTP Request
    """
    return render_to_response('fall-midterm.html',
                              {},
                              context_instance=RequestContext(request))

def quiz(request):
    """
    Displays a full quiz if user is logged in to DLS; otherwise
    just display the public example views.

    :param request: HTTP request
    """
    quiz,questions = get_test_questions(request)
    return render_to_response('assessment-quiz.html',
                              {'questions':questions,
                               'quiz':quiz,
                               'section':'assessment'},
                              context_instance=RequestContext(request))

def fail_exercise(request):
    return render_to_response('fail-essay.html',
                              {'section':'assessment'},
                              context_instance=RequestContext(request))



def job_exercise(request):
    return render_to_response('lib-sys-job-exercise.html',
                              {'section':'assessment'},
                              context_instance=RequestContext(request))

def project(request):
    return render_to_response('project-assessment.html',
                              {'section':'assessment'},
                              context_instance=RequestContext(request))



def quizzes(request):
    quizzes = Test.objects.filter(category="qz")
    return render_to_response('quizzes.html',
                              {'quizzes':quizzes,
                               'section':'assessment'},
                              context_instance=RequestContext(request))


