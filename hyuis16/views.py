
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authen.models import hyu_users
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from board.models import board


def index(request):
    notice = board.objects.all().filter(category_id=1)[:6]
    free_board = board.objects.all().filter(category_id=2)[:6]

    return render(request, 'index.html', {'notices': notice, 'frees':free_board})


@require_http_methods(["GET", "POST"])
def login(request):
    userid = request.POST['user_id']
    pw = request.POST['password']

    try:
        m = hyu_users.objects.get(user_id=userid)
    except:
        return HttpResponse('not matching id')

    if m.password == pw:
        username = m.user_name
        request.session['member'] = userid


        return HttpResponseRedirect(reverse('home'))
    else :
        return HttpResponse('not matching pw')

def logout(request):
    try:
        del request.session['member']
    except :
        return HttpResponse('logout fail')
    return HttpResponseRedirect(reverse('home'))




