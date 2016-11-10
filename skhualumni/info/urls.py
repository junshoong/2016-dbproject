from django.conf.urls import url
from info.views import *

urlpatterns = [
    url(r'^$', render_greeting, name='home'),
    url(r'^greeting/$', render_greeting, name='greeting'),
    url(r'^business/$', render_business, name='business'),
    url(r'^organization/$', render_organization, name='organization'),
    url(r'^map/$', render_map, name='map'),
    url(r'^usage/$', render_usage, name='usage'),
]
