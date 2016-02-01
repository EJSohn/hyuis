# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from .models import hyu_users
from django.http import HttpResponse

# Create your views here.

def register(request):
    return render(request, 'authen/register.html')

def register_user(request):
    user_id = request.POST['user_id']
    user_name = request.POST['user_name']
    pw = request.POST['password']
    admin_year = request.POST['admission_year']
    phone = request.POST['phone_number']
    self = request.POST['self_introduce']

    # 비밀번호 암호화 처리는 나중에..

    user = hyu_users(user_id=user_id, user_name=user_name, password=pw, admission_year=admin_year, phone_number=phone,
                 self_introduce=self)


    user.save()
    return redirect('register_succeed')


def register_succeed(request):
    return render(request, 'authen/register.html')

def mypage(request):
    return render(request, 'authen/mypage.html')

def modify(request):
    return render(request, 'authen/modify.html')

def myposts(request):
    return render(request, 'authen/myposts.html')