from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from board.views import *

urlpatterns = [
    url(r'^$', index, name='index'),    # 글 목록
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),    # 글 내용
    url(r'^(?P<pk>\d+)/comments/new/$', comment_new, name='comment_new'),    #댓글 작성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', comment_edit, name='comment_edit'),     #댓글 수정
    url(r'^post/new/$', post_new, name='post_new'),     # 새 포스팅 등록
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
