from django.conf.urls import url
from alumni.views import UserLV, ExecutiveLV, UserDV

urlpatterns = [
    url(r'^$', UserLV.as_view(), name='index'),
    url(r'^executive/$', ExecutiveLV.as_view(), name='executive'),
    url(r'^(?P<pk>\d+)/$', UserDV.as_view(), name='detail'),
]
