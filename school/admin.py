from django.contrib import admin
from models import *

class SchoolAdmin(admin.ModelAdmin):
    model = School
    list_display = ("name", "city", "county", "state")
    # list_filter  = ("party","district","state",)

admin.site.register(School, SchoolAdmin)
admin.site.register(State)
