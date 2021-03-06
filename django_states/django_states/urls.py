from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from main.views import GetPost, StateListView, CityDetailView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_states.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^first_view/(?P<starts_with>\w+)/$', 'main.views.first_view'),
    url(r'^first_view/$', 'main.views.first_view'),
    url(r'^get_post/$', 'main.views.get_post'),
    url(r'^template_view/$', 'main.views.template_view'),
    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^GetPost/$', csrf_exempt(GetPost.as_view())),
    url(r'^state_list_view/$', StateListView.as_view()),
    url(r'^cities/(?P<pk>[0-9]+)/$', CityDetailView.as_view()),
    
)
