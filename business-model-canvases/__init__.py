#-------------------------------------------------------------------------------
# Name:        Business Modal Canvas Utilities
# Purpose:     Business Modal Canvas Utilities
#
# Author:      Jeremy Nelson
#
# Created:     2014/07/09
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     GPLv2
#-------------------------------------------------------------------------------
import datetime
import json
import rdflib

SCHEMA_NS = rdflib.Namespace('http://schema.org/')
SCHEMA_RDF = rdflib.Graph().parse('http://schema.rdfs.org/all.rdf')

def add_activity(**kwargs):
    activity = kwargs
    if not 'name' in activity:
        activity['name'] = raw_input("Enter name of activity>>")
    if not '@id' in activity:
        activity['@id'] = slugify(activity['name'])
    return activity

def base_biz_model_canvas(name):
    bmc = {"@type": "BusinessModelCanvas",
           "@context": {
               "@vocab": "http://schema.org/",
               "activity": None,
               "channel": None,
               "cost": None,
               "customer-relationship": None,
               "customer-segment": None,
               "partner": None,
               "proposition": None,
               "resource": None,
               "revenue-stream": None},
           "activity": [],
           "channel": [],
           "creator": None,
           "cost": [],
           "customer-relationship": [],
           "customer-segment": [],
           "dateCreated": datetime.datetime.utcnow().strftime("%Y-%m-%d"),
           "name": name,
           "partner": [],
           "proposition": [],
           "resource": [],
           "revenue-stream": []}
    return bmc

def choose_action():
    subclass = rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf')
    for subject in SCHEMA_RDF.subjects(
        predicate=subclass,
        object=rdflib.term.URIRef(u'http://schema.org/Action')):
        print(schema_owl.value(subject=s, predicate=rdflib.RDFS.label))
        children = [child for child in schema_owl.subjects(
            predicate=rdflib.URIRef('http://www.w3.org/2000/01/rdf-schema#subClassOf'),
            object=subject)]
        for i, child in enumerate(children):
            print("\t{} - {}".format(
                i,
                SCHEMA_RDF.value(
                    subject=child,
                    predicate=rdflib.RDFS.label)))
        prompt = raw_input("Select number or press <ENTER>")
        if len(prompt) < 1:
            pass
        else:
            print("You selected {}".format(children[int(prompt)]))
            return str(children[int(prompt)]))