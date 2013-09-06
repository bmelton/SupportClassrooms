from tastypie.resources import ModelResource
from models import Director

class DirectorResource(ModelResource):
    class Meta:
        queryset = Director.objects.all()
        resource_name = 'directors'
