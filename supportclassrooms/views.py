from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from school.views import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from school.models import School
from school.serializers import SchoolSerializer
from lists.serializers import *

def home(request):
    return render(request, "index.html", {
        "compressed" : settings.COMPRESSED,
    })

def grades(request):
    return render(request, "index.html", {
        "compressed" : settings.COMPRESSED,
    })

@csrf_exempt
def get_school(request, uuid):
    if request.method == 'GET':
        school = School.objects.get(uid=uuid)
        serializer = SchoolSerializer(school)
        return JSONResponse(serializer.data)

@csrf_exempt
def list_schools(request):
    if request.method == 'GET':
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def list_categories(request, school=None):
    if request.method == "GET":
        if not school:
            categories = Category.objects.all()
        else:
            categories = Category.objects.filter(school__uid=school)
        serializer = CategorySerializer(categories, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def list_lists(request, school=None, cat=None):
    if request.method == "GET":
        if not school:
            lists = List.objects.all()
        else:
            if not cat:
                lists = List.objects.filter(school__uid=school, active=True, category=None)
            else:
                lists = List.objects.filter(school__uid=school, active=True, category=cat)
        serializer = ListSerializer(lists, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def list_items(request, list):
    if request.method == "GET":
        items = Item.objects.filter(list=list)
        serializer = ItemSerializer(items, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def get_list(request, list):
    if request.method == "GET":
        list = List.objects.get(id=list)
        serializer = ListSerializer(list)
        return JSONResponse(serializer.data)


