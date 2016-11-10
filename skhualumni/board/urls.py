from django.conf.urls import url
from board.views import *

urlpatterns = [
    url(r'^$', index, name='index'),    # 글 목록
    url(r'^(?P<pk>\d+)/$', post_detail, name='detail'),    # 글 내용
    url(r'^new/$', post_new, name='new'),     # 새 포스팅 등록
]
