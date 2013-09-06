import datetime
from haystack import indexes
from school.models import State, School

class SchoolIndex(indexes.SearchIndex, indexes.Indexable):
    text    = indexes.CharField(document=True, use_template=True)
    name    = indexes.CharField(model_attr='name')
    address = indexes.CharField(model_attr='address')
    address2= indexes.CharField(model_attr='address2')
    county  = indexes.CharField(model_attr='county')
    state   = indexes.CharField(model_attr='state')
    zipcode = indexes.CharField(model_attr='zipcode')

    def get_model(self):
        return School
