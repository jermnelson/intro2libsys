"""
 `mod`:views Introduction to Library Systems Syllabus Views
"""
__author__ = 'Jeremy Nelson'
from django.shortcuts import render_to_response
from django.template import RequestContext
from syllabus.models import *
from intro.models import Instructor
from assessment.models import Exercise,Test
import datetime

def get_class_range(class_query):
    """
    Helper function takes a ClassDate query and returns a
    list of the dicts for each class.

    :param class_query: ClassDate query
    :rtype list: List of dicts for each class session
    """
    classes = []
    for date in class_query:
        class_info = {'date':date}
        class_info['chapters'] = TextbookChapter.objects.filter(class_date=date.pk)
        class_info['exercise'] = Exercise.objects.filter(date_of=date.pk)
        class_info['readings'] = Reading.objects.filter(class_date=date.pk).order_by('title')
        class_info['test'] = Test.objects.filter(date_of=date.pk)
        classes.append(class_info)
    return classes

def home(request):
    """
    Default view for Introduction to Library Systems Course

    :param request: HTTP request
    """
    return render_to_response('syllabus.html',
                             {'classes':get_class_range(ClassDate.objects.all().order_by('start')),
                              'readings_by_alpha':Reading.objects.order_by('title'),
                              'section':'syllabus',
                              'timestamp':datetime.datetime.today()},
                              context_instance=RequestContext(request))

def instructor(request):
    """
    Default view for Instructor contact

    :param request: HTTP request
    """
    instructor = Instructor.objects.all()
    return render_to_response('instructor-contact.html',
                              {'instructor':instructor,
                               'section':'syllabus'},
                              context_instance=RequestContext(request))


def month(request,year,month):
    """
    Displays all of the sessions for one month.

    :param request: HTTP Request
    :param year: Year in YYYY format
    :param month: Month in 01-12 format
    """
    question_date = datetime.datetime(year=int(year),
                                      month=int(month),
                                      day=1)
    next_date = question_date + datetime.timedelta(30)
    class_dates = ClassDate.objects.filter(start__gte=question_date
    ).filter(end__lte=next_date).order_by('start')
    return render_to_response('syllabus-month.html',
                             {'classes':get_class_range(class_dates),
                              'month':(question_date,next_date),
                              'readings_by_alpha':Reading.objects.order_by('title'),
                              'section':'syllabus',
                              'timestamp':datetime.datetime.today()},
                              context_instance=RequestContext(request))

def project(request):
    """
    Displays project view.

    :param request: HTTP Request
    """
    return render_to_response('project.html',
                              {'section':'syllabus'},
                              context_instance=RequestContext(request))



def session(request,year,month,day):
    """
    Displays course work and associated streams for a single
    class session.

    :param request: HTTP Request
    :param year: Year in YYYY format
    :param month: Month in 01-12 format
    :param day: Day in 01-31 format
    """
    question_date = datetime.datetime(year=int(year),
                                      month=int(month),
                                      day=int(day))
    next_date = question_date + datetime.timedelta(1)
    class_date = ClassDate.objects.filter(start__gte=question_date
    ).filter(end__lte=next_date)
    assessments = []
    exercises = Exercise.objects.filter(date_of=class_date[0].pk)
    for row in exercises:
        assessments.append(row)
    tests = Test.objects.filter(date_of=class_date[0].pk)
    for row in tests:
        assessments.append({"value":row.get_category_display()})
    return render_to_response('syllabus-session.html',
                              {'assessments':assessments,
                               'chapters':TextbookChapter.objects.filter(class_date=class_date[0].pk),
                               'date_of':question_date,
                               'readings':Reading.objects.filter(class_date=class_date[0].pk),
                               'section':'syllabus',
                               'videos':Video.objects.filter(class_date=class_date[0].pk)
                              },
                              context_instance=RequestContext(request))
    
def year(request,year):
    """
    Displays all sessions for a year

    :param request: HTTP Request
    :param year: Year in YYYY format
    """
    start_date = datetime.datetime(year=int(year),
                                   month=1,
                                   day=1)
    end_date = datetime.datetime(year=int(year),
                                 month=12,
                                 day=31)
    class_dates = ClassDate.objects.filter(start__gte=start_date
    ).filter(end__lte=end_date)
                                   
    return render_to_response('syllabus-year.html',
                              {'classes':class_dates,
                               'section':'syllabus',
                               'year':year},
                              context_instance=RequestContext(request))

