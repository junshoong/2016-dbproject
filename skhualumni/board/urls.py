from django.conf.urls import url
from board.views import *

urlpatterns = [
    url(r'^$', index, name='index'),    # 글 목록
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),    # 글 내용
    url(r'^(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),   # 글 수정
    url(r'^new/$', post_new, name='post_new'),     # 새 글 등록
    url(r'^search/$', PostSearch.as_view(), name='post_search'),  # 글 검색
    url(r'^(?P<pk>\d+)/delete/$', post_delete, name='post_delete'),  # 글 삭제
    url(r'^(?P<pk>\d+)/comments/new/$', comment_new, name='comment_new'),    # 댓글 작성
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', comment_edit, name='comment_edit'),     # 댓글 수정
]
