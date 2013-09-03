from tastypie.resources import ModelResource
from models import Resource

class StudyResource(ModelResource):
    class Meta:
        queryset = Resource.objects.all()
        resource_name = 'study'



