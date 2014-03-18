from django.conf.urls import patterns, include, url
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from resources.api import StudyResource
from officers.api import OfficerResource
from directors.api import DirectorResource
from news.api import NewsResource
from school.api import SchoolResource
v1_api = Api(api_name='v1')

v1_api.register(StudyResource())
v1_api.register(OfficerResource())
v1_api.register(DirectorResource())
v1_api.register(NewsResource())
v1_api.register(SchoolResource())

urlpatterns = patterns('',
    url(r'^$',                                          'supportclassrooms.views.home',                 name='home'),
    url(r'^grades/$',                                   'supportclassrooms.views.grades',               name='grades'),
    url(r'^api/schools/list/$',                         'supportclassrooms.views.list_schools',         name='list_schools'),
    url(r'^api/schools/(?P<uuid>[-\w]+)/$',             'supportclassrooms.views.get_school',           name='get_school'),

    url(r'^search/',include('haystack.urls')),
    # (r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',   include(v1_api.urls)),
)
