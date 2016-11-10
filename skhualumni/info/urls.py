from django.conf.urls import url
from alumni.views import UserDV

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', UserDV.as_view(), name='detail'),
]
