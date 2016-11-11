from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from board.views import *

urlpatterns = [
    url(r'^$', index, name='index'),    # 글 목록
    url(r'^(?P<pk>\d+)/$', post_detail, name='detail'),    # 글 내용
    url(r'^(?P<pk>\d+)/comments/new/$', comment_new, name='detail'),    #댓글 작성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', comment_edit, name='detail'),     #댓글 수정

    url(r'^new/$', post_new, name='new'),     # 새 포스팅 등록
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
