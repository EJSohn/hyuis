from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register/user$', views.register_user, name='register_user'),
    url(r'^register/user/succeed', views.register_succeed, name='register_succeed')
]