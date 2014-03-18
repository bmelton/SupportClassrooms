from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from school.views import JSONResponse
from django.views.decorators.csrf import csrf_exempt
from school.models import School
from school.serializers import SchoolSerializer

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

