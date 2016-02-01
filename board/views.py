from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import board, category
from authen.models import hyu_users
from django.core.urlresolvers import reverse

# Create your views here.

def free_board(request):
    return render(request, 'board/board.html')

def review(request):
    return render(request, 'board/review.html')

def review_post(request):
    return render(request, 'board/review_post.html')

def post(request):
    return render(request, 'board/post.html')

def write(request):
    return render(request, 'board/write.html')

def mypage(request):
    return render(request, 'board/mypage.html')

def writing(request):

    today = datetime.today()

    category_id = request.POST['category_id']
    user_id = request.session['member']

    title = request.POST['title']
    content = request.POST['content']
    created_date = today

    post = board(title=title, content=content, created_date=created_date)

    cate = category.objects.get(category_id=category_id)
    user = hyu_users.objects.get(user_id=user_id)
    post.category_id = cate
    post.user_id = user
    post.save()

    return HttpResponseRedirect(reverse('board:entire_view'))
