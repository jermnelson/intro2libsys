__author__ = "Jeremy Nelson"
import json
import os
from django.views.generic.simple import direct_to_template
from django.http import Http404, HttpResponse

from intro.settings import PROJECT_HOME
RESOURCES = {}
RESOURCES_DIR = os.path.join(PROJECT_HOME,
                             "resources",
                             "fixures")
for filename in next(os.walk(RESOURCES_DIR))[2]:
    if filename.endswith(".json"):
        resource = json.load(open(os.path.join(RESOURCES_DIR,
                                               filename),
                                  "rb"))
        resource_id = resource.get('@id').split("//")[-1]
        RESOURCES[resource_id] = resource
                                               

def detail(request, resource_id):
    direct_to_template(request,
                       'resource-detail',
                       {})

def home(request):
    return direct_to_template(request,
                             'resource-home.html',
                             {'resources':RESOURCES.values()})


