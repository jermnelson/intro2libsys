__author__ = "Jeremy Nelson"

from django.shortcuts import render_to_response
from django.template import RequestContext
from intro.settings import PROJECT_HOME
from textbook.models import Chapter,Page
from intro.views import json_view
import markdown,os

def chapter(request,number="1"):
    chapter = Chapter.objects.get(pk=number)
    return render_to_response('chapter.html',
                              {'chapter':chapter,
                               'chapters':Chapter.objects.all()},
                              context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html',
                              {'chapters':Chapter.objects.all()},
                              context_instance=RequestContext(request))

@json_view
def page(request):
    page_pk = request.REQUEST.get('pk')
    page = Page.objects.get(pk=page_pk)
    page_path = "{0}{1}".format(os.path.join(PROJECT_HOME,
	                                     "textbook"),
	                        page.location)
    print("{0} {1}".format(PROJECT_HOME,page_path))
    page_contents = open(page_path,"rb").read()
    html = markdown.markdown(page_contents)
    output = {'html':html}
    return output
