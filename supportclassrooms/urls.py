from django.conf.urls import patterns, include, url
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from resources.api import StudyResource
from officers.api import OfficerResource
from directors.api import DirectorResource
from news.api import NewsResource
v1_api = Api(api_name='v1')

v1_api.register(StudyResource())
v1_api.register(OfficerResource())
v1_api.register(DirectorResource())
v1_api.register(NewsResource())

urlpatterns = patterns('',
    url(r'^$', 'supportclassrooms.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',   include(v1_api.urls)),
)
