from django.conf.urls import url

from snippets.views import *
from snippets import models
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



app_name = 'snippets'
urlpatterns = [
    
   
    url(r'^snippets/$', views.index),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)