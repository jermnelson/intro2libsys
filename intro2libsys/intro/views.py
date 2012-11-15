"""
 `mod`:views Introduction to Library Systems Views
"""
__author__ = 'Jeremy Nelson'
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from Curriculum.models import CourseSession
import datetime,sys,logging,json

def about(request):
    """
    About Introduction to Library Systems Distributed Learning System
    """
    return render_to_response('about.html',
                              {},
                              context_instance=RequestContext(request))

def home(request):
    """
    Default view for Introduction to Library Systems Course
    """
    sessions = CourseSession.objects.all()
    return render_to_response('index.html',
                             {'sessions':sessions,
                              'timestamp':datetime.datetime.today()},
                             context_instance=RequestContext(request))

def json_view(func):
    """
    Returns JSON results from method call, from Django snippets
    `http://djangosnippets.org/snippets/622/`_
    """
    def wrap(request, *a, **kw):
        response = None
        try:
            func_val = func(request, *a, **kw)
            assert isinstance(func_val, dict)
            response = dict(func_val)
            if 'result' not in response:
                response['result'] = 'ok'
        except KeyboardInterrupt:
            raise
        except Exception,e:
            exc_info = sys.exc_info()
            print(exc_info)
            logging.error(exc_info)
            if hasattr(e,'message'):
                msg = e.message
            else:
                msg = ugettext("Internal error: %s" % str(e))
            response = {'result': 'error',
                        'text': msg}
            
        json_output = json.dumps(response)
        return HttpResponse(json_output,
                            mimetype='application/json')
    return wrap
