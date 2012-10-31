"""
 `mod`:views DU ASIS&T Student Chapter TechBytes
"""
__author__ = "Jeremy Nelson"

from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    """
    Home view for TechBytes Presentation

    :param request:
    """
    return render_to_response('library-as-a-start-up.html',
                              {},
                              context_instance=RequestContext(request))
