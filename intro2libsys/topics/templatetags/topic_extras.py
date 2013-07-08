__author__ = "Jeremy Nelson"
import json
import os

from django.template import Context,Library,loader
from django.utils.safestring import mark_safe
from assessment.models import Test
from intro.settings import PROJECT_HOME

register = Library()

def get_resource(resource_name):
    """
    Retrieves the JSON-LD of a resource, returns generated html from a
    template for this resource.

    :param test_type: resource_name
    """
    output = ''
    resource_path = os.path.join(PROJECT_HOME, 
                                 "resources", 
                                 "fixures", 
                                 "{0}.json".format(resource_name))
    if os.path.exists(resource_path):
        resource = json.load(open(resource_path, 'rb'))
        summary_template = loader.get_template('resource-summary.html')
        output = summary_template.render(Context({'resource': resource,
                                                  'id': resource.get('@id')}))
    return mark_safe(output)
    


register.filter('get_resource', get_resource)
