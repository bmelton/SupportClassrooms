from django.forms import widgets
from rest_framework import serializers
from models import School

class SchoolSerializer(serializers.ModelSerializer):
    state = serializers.Field(source='state.name')
    class Meta:
        model = School
        fields = ('uid', 'name', 'address', 'address2', 'county', 'city', 'state', 'zipcode', 'background', 'principal', 'website', 'phone', 'fax',)
