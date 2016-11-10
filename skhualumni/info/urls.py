from django.conf.urls import url
from info import views

urlpatterns = [
    url(r'^$', views.greet, name='home'),
    url(r'^greeting/$', views.greet, name='greeting'),
    # url(r'^$', GreetingView.as_view(), name='home'),
    # url(r'^greeting/$', GreetingView.as_view(), name='greeting'),
    # url(r'^business/$', BusinessView.as_view(), name='business'),
    # url(r'^organization/$', OrganizationView.as_view(), name='organization'),
    # url(r'^map/$', MapView.as_view(), name='map'),
    # url(r'^usage/$', UsageView.as_view(), name='usage'),
]
