"""
 `mod`:views DU ASIS&T Student Chapter TechBytes
"""
__author__ = "Jeremy Nelson"

from django.shortcuts import render_to_response
from django.template import RequestContext

def cc_marcr_apps(request):
    """
    Colorado College's Redis-based MARCR Datastore and Library Apps
    Project

    :param request:
    """
    return render_to_response('cc-marcr-ds-lib-apps.html',
                              {'section':'presentation'},
                              context_instance=RequestContext(request))

def frbr_rda_marcr(request):
    """
    FRBR, RDA, and MARCR view for TechBytes Presentation

    :param request:
    """
    return render_to_response('frbr-rda-marcr.html',
                              {'section':'presentation'},
                              context_instance=RequestContext(request))

def home(request):
    """
    Home view for TechBytes Presentation

    :param request:
    """
    return render_to_response('library-as-a-start-up.html',
                              {'section':'home'},
                              context_instance=RequestContext(request))

def leanstartup(request):
    """
    Lean Startup view for TechBytes Presentation

    :param request:
    """
    return render_to_response('lean-startup.html',
                              {'section':'presentation'},
                              context_instance=RequestContext(request))


def orgmap(request):
    """
    Organizational Map view for TechBytes Presentation

    :param request:
    """
    return render_to_response('org-map.html',
                              {'section':'presentation'},
                              context_instance=RequestContext(request))
