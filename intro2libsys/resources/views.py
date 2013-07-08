__author__ = "Jeremy Nelson"
import json
import os
from django.shortcuts import render
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
        resource_id = os.path.split(resource.get('@id'))[-1]
        RESOURCES[resource_id] = resource
                                               

def detail(request, resource_id):
    resource = RESOURCES[resource_id]
    return render(request,
                  'resource-detail.html',
                  {'resource': resource,
                   'resource_class': resource.get('@type')})

def home(request):
    return render(request,
                  'resource-home.html',
                  {'resources':RESOURCES.values()})


