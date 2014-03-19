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
from amazon import views

v1_api = Api(api_name='v1')

v1_api.register(StudyResource())
v1_api.register(OfficerResource())
v1_api.register(DirectorResource())
v1_api.register(NewsResource())
v1_api.register(SchoolResource())

urlpatterns = patterns('',
    url(r'^$',                                                      'supportclassrooms.views.home',                 name='home'),
    url(r'^grades/$',                                               'supportclassrooms.views.grades',               name='grades'),

    url(r'^api/checkout/(?P<list>[\d]+)/$',                         'amazon.views.checkout_for_list'),

    # Schools
    url(r'^api/schools/list/$',                                     'supportclassrooms.views.list_schools',         name='list_schools'),
    url(r'^api/schools/(?P<uuid>[-\w]+)/$',                         'supportclassrooms.views.get_school',           name='get_school'),
    
    # Categories
    url(r'^api/categories/list/$',                                  'supportclassrooms.views.list_categories',      name='list_categories'),
    url(r'^api/categories/list/(?P<school>[-\w]+)/$',               'supportclassrooms.views.list_categories',      name='list_categories'),

    # Lists
    url(r'^api/lists/(?P<list>[\d]+)/$',                            'supportclassrooms.views.get_list',             name='get_list'),
    url(r'^api/lists/list/$',                                       'supportclassrooms.views.list_lists',           name='list_lists'),
    url(r'^api/lists/list/(?P<school>[-\w]+)/$',                    'supportclassrooms.views.list_lists',           name='list_lists'),
    url(r'^api/lists/list/$',                                       'supportclassrooms.views.list_lists',           name='list_lists'),
    url(r'^api/lists/list/(?P<school>[-\w]+)/(?P<cat>[-\w]+)/$',    'supportclassrooms.views.list_lists',           name='list_lists'),

    # Items
    url(r'^api/items/list/(?P<list>[\d]+)/$',                       'supportclassrooms.views.list_items',           name='list_items'),

    url(r'^search/',include('haystack.urls')),
    # (r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/',   include(v1_api.urls)),
)
