__author__ = "Jeremy Nelson"

from django.shortcuts import render_to_response
from django.template import RequestContext
from intro.settings import PROJECT_HOME
from textbook.models import Chapter,Page
from intro.views import json_view
import markdown,os,logging

def get_chapters():
    chapters = Chapter.objects.all()
    for chapter in chapters:
        chapter.pages = Page.objects.filter(chapter=chapter).order_by('order')
    return chapters

def chapter(request,
            number="1"):
    chapter = Chapter.objects.get(pk=number)
    first_page_query = Page.objects.filter(chapter=chapter,
                                           order=1)
    if len(first_page_query) > 0:
        chapter.first_page = first_page_query[0]
    return render_to_response('chapter.html',
                              {'chapter':chapter,
                               'chapters':get_chapters()},
                              context_instance=RequestContext(request))

def home(request):
    
    return render_to_response('home.html',
                              {'chapters':get_chapters()},
                              context_instance=RequestContext(request))

@json_view
def page(request):
    page_pk = request.REQUEST.get('pk')
    page = Page.objects.get(pk=page_pk)
    page_path = os.path.join(PROJECT_HOME,
                             "textbook",
                             "fixures",
                             "content",
                             page.location)
    page_contents = open(page_path,"rb").read()
    html = markdown.markdown(page_contents)
    next_page = Page.objects.filter(chapter=page.chapter).filter(order=page.order + 1)
    if len(next_page) > 0:
        next_page = next_page[0].pk
    else:
        next_page = None
    previous_page = Page.objects.filter(chapter=page.chapter).filter(order=page.order - 1)
    if len(previous_page) > 0:
        previous_page = previous_page[0].pk
    else:
        previous_page = None
    if len(page.title) < 1:
        page.title = page.chapter.title
    output = {'html':html,
              'next':next_page,
              'previous':previous_page,
              'title':page.title}
    return output
