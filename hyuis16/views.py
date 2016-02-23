
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authen.models import hyu_users
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from board.models import board, imghandler
from datetime import datetime


def index(request):
    notice = board.objects.all().filter(category_id=1).order_by('-post_id')[:6]
    free_board = board.objects.all().filter(category_id=2).order_by('-post_id')[:6]
    review = imghandler.objects.all().filter(post_id__category_id=4).order_by('-post_id')[:4]
    today = datetime.today().date()

    return render(request, 'index.html', {'notices': notice, 'frees':free_board, 'reviews':review, 'today':today})


@require_http_methods(["GET", "POST"])
def login(request):
    userid = request.POST.get('user_id',False)
    pw = request.POST.get('user_pw',False)

    try:
        m = hyu_users.objects.get(user_id=userid)
    except:
        return HttpResponse('Wrong ID')

    if m.password == pw:
        username = m.user_name
        request.session['member'] = userid


        return HttpResponse('success')
    else :
        return HttpResponse('Wrong PW')

def logout(request):
    try:
        del request.session['member']
    except :
        return HttpResponse('logout fail')
    return HttpResponseRedirect(reverse('home'))




