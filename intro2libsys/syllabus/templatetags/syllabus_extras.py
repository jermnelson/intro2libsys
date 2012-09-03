__author__ = "Jeremy Nelson"

from django.template import Context,Library,loader
from django.utils.safestring import mark_safe
from assessment.models import Test

register = Library()

def get_test_type(test):
    """
    Iterates through Test.type_of choices.

    :param test_type: 2 char test type 
    """
    
    for row in Test.get_category_display():
        if row[0] == test_type:
            return mark_safe(row[1])
    


register.filter('get_test_type',get_test_type)
