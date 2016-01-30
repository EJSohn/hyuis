from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.board ,name='board'),
    url(r'^free/', views.free_board, name='free board'),
    url(r'^review/', views.review, name='review'),
    url(r'^review_post/', views.review_post, name='review_post'),
    url(r'^post/', views.post, name='post'),
    url(r'^write/', views.write, name='write'),
]