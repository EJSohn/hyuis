from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.some_board ,name=''),
    url(r'^entire_view/', views.entire_board, name='entire_view'),
    url(r'^notice/([0-4]{1})/', views.some_board, name='notice'),
    url(r'^free/([0-4]{1})/', views.some_board, name='free board'),
    url(r'^review/', views.review, name='review'),
    url(r'^review_post/', views.review_post, name='review_post'),
    url(r'^post/', views.post, name='post'),
    url(r'^write/$', views.write, name='write'),
    url(r'^write/writing$', views.writing, name='writing'),
    url(r'^mypage/', views.mypage, name='mypage'),
    ]
