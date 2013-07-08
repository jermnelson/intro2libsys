"Resource Extras are custom tags for Resource Display in Intro2libsys"
__author__ = "Jeremy Nelson"

from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter(is_safe=True)
def get_annotations(resource):
    "Filter extracts and displays annotations"
    output = ''
    annotation_template = template.loader.get_template(
        'resources/annotation.html')
    annotations = resource.get('oa:Annotation', [])
    for annotation in annotations:
        simple_annotation = {}
        for key, value in annotation.iteritems():
            simple_annotation[key.split(":")[-1]] = value
        output += annotation_template.render(
            template.Context({'annotation': simple_annotation}))
    return mark_safe(output)
