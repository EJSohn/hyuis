from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.mypage ,name='mypage'),
    url(r'^mypage/', views.myprofile, name='myprofile'),
]