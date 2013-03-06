"""
 :mod:`forms` Forms for performing CRUD operations on Intro2LibSys Resources
"""
from wtforms import Form, BooleanField, SelectField, TextField, validators
from aristotle.bibframe.models import Holding, Instance, Organization, Person, Work

class ResourceForm(Form):
    """
    `ResourceForm` 
    """
    name = TextField('Name', [validators.Length(min=4, max=20)])
    url = TextField('URL', [validators.Length(min=10, max=255)])

class CreativeWorkForm(ResourceForm):
    """
    `WorkForm`
    """
    datePublished = TextField('Date published', [validators.Length(min=4, max=26)])
    work_type = SelectField(u'Creative Work Type:', choices=[])
    
    
