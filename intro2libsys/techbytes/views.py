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

def consortium_marcr_ds_hybrid_cloud(request):
    """
    Evolving towards a Consortium MARCR Datastore Hybrid-Cloud
    view

    :param request:
    """
    return render_to_response('consortium-marcr-datastore-hybrid-cloud.html',
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

def glossary(request):
    """
    Glossary of terms uses view for TechBytes Presentation

    :param request:
    """
    return render_to_response('glossary.html',
                              {'section':'addendum'},
                              context_instance=RequestContext(request))

def home(request):
    """
    Home view for TechBytes Presentation

    :param request:
    """
    return render_to_response('library-as-a-start-up.html',
                              {'section':'home'},
                              context_instance=RequestContext(request))

def leader_summary(request):
    """
    Leader summary view for TechBytes Presentation

    :param request:
    """
    return render_to_response('summary.html',
                              {'section':'addendum',
                               'title':'Leader Summary'},
                              context_instance=RequestContext(request))

def leanstartup(request):
    """
    Lean Startup view for TechBytes Presentation

    :param request:
    """
    return render_to_response('lean-startup.html',
                              {'section':'presentation'},
                              context_instance=RequestContext(request))


def manager_summary(request):
    """
    Manager summary view for TechBytes Presentation

    :param request:
    """
    return render_to_response('summary.html',
                              {'section':'addendum',
                               'title':'Manager Summary'},
                              context_instance=RequestContext(request))


def orgmap(request):
    """
    Organizational Map view for TechBytes Presentation

    :param request:
    """
    return render_to_response('org-map.html',
                              {'section':'presentation'},
                              context_instance=RequestContext(request))

def resources(request):
    """
    Resources references or used view for TechBytes Presentation

    :param request:
    """
    return render_to_response('resources.html',
                              {'section':'addendum'},
                              context_instance=RequestContext(request))


def task_summary(request):
    """
    Tasks summary view for TechBytes Presentation

    :param request:
    """
    return render_to_response('summary.html',
                              {'section':'addendum',
                               'title':'Task Summary'},
                              context_instance=RequestContext(request))
