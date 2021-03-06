from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.some_board ,name=''),
    url(r'^entire_view/', views.entire_board, name='entire_view'),

    url(r'^notice/([0-5]{1})/$', views.depth_board, name='notice'),
    url(r'^notice/([0-9]{1})/$', views.some_board, name='notice_deep'),

    url(r'^freeboard/([0-5]{1})/', views.some_board, name='freeboard'),
    url(r'^review/', views.review, name='review'),
    #url(r'^review_post/', views.review_post, name='review_post'),

    url(r'^tip/([0-5]{1})/$', views.depth_board, name='tip'),
    url(r'^tip/([0-9]{1})/$', views.some_board, name='tip_deep'),

    url(r'^post/([0-9]+)/$', views.post, name='post'),
    url(r'^post/([0-9]+)/comment$', views.commenting, name='comment'),
    url(r'^post/recomment$', views.recomment, name="recomment"),
    url(r'^write/$', views.write, name='write'),
    url(r'^write/writing$', views.writing, name='writing'),
    url(r'^write/modifying/([0-9]+)/$', views.modifying, name='modifying'),
    url(r'^mypage/', views.mypage, name='mypage'),
    url(r'^post/([0-9]+)/delete$', views.post_delete, name='post_delete'),
    url(r'^post/([0-9]+)/modify$', views.post_modify, name='post_modify' ),
    url(r'^post/([0-9]+)/comment/delete/$', views.comment_delete, name='comment_delete'),
    url(r'^post/([0-9]+)/comment/update/$', views.comment_update, name='comment_update'),
    ]
