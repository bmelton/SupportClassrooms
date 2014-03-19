from django.forms import widgets
from rest_framework import serializers
from models import Category, List, Item

class CategorySerializer(serializers.ModelSerializer):
    school      = serializers.Field(source='school.name')
    class Meta:
        model   = Category
        fields  = ('id', 'school', 'name', 'list_count', 'active',)

class ListSerializer(serializers.ModelSerializer):
    school      = serializers.Field(source='school.name')
    category    = serializers.Field(source='category.name')
    class Meta:
        model   = List
        fields  = ('id', 'school', 'category', 'name', 'active',)

class ItemSerializer(serializers.ModelSerializer):
    school      = serializers.Field(source='school.name')
    category    = serializers.Field(source='category.name')
    list        = serializers.Field(source='list.name')
    class Meta:
        model = Item
        fields = ('id', 'school', 'category', 'name', 'url', 'image', 'price', )
