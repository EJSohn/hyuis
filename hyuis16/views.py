
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authen.models import hyu_users
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def login(request):
    userid = request.POST['user_id']
    pw = request.POST['password']

    try:
        m = hyu_users.objects.get(user_id=userid)
    except:
        return HttpResponse('not matching id')

    if m.password == pw:
        username = m.user_id
        request.session['member'] = username

        return HttpResponseRedirect(reverse('home'))
    else :
        return HttpResponse('not matching pw')

def logout(request):
    try:
        del request.session['member']
    except :
        return HttpResponse('logout fail')
    return HttpResponseRedirect(reverse('home'))


