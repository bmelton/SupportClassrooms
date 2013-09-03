from tastypie.resources import ModelResource
from models import Officer

class OfficerResource(ModelResource):
    class Meta:
        queryset = Officer.objects.all()
        resource_name = 'officers'



