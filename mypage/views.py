from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.


def mypage(request):
    return HttpResponse('mypage entire view')

def myprofile(request):
    return render(request, 'mypage/mypage.html')