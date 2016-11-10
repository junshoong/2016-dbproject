from django.conf.urls import url
from alumni.views import UserLV, UserDV

urlpatterns = [
    url(r'^$', UserLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', UserDV.as_view(), name='detail'),
]
