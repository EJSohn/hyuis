
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from authen.models import hyu_users
from django.http import HttpResponse


def index(request):
    if request.session['loged_member'] :
        login_flag = 'yes'
    else :
        login_flag = 'no'
    return render(request, 'index.html', {'flag':login_flag})


@require_http_methods(["GET", "POST"])
def login(request):
    userid = request.POST['user_id']
    pw = request.POST['password']

    try:
        m = hyu_users.objects.get(user_id=userid)
    except:
        return HttpResponse('not matching id')

    if m.password == pw:
        request.session['loged_member'] = m.user_name
        return HttpResponse('loged in')
    else :
        return HttpResponse('not matching pw')

def logout(request):
    try:
        del request.session['logged_member']
    except KeyError:
        pass
    return render(request, 'index.html')


