# -*- coding: utf-8  -*-
from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import board, category
from authen.models import hyu_users
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import board

# Create your views here.

#전체게시판
def entire_board(request):
    all_list = board.objects.all()
    paginator = Paginator(all_list, 10)

    page = request.GET.get('page')
    try:
        all_post = paginator.page(page)
    except PageNotAnInteger:
        all_post = paginator.page(1)
    except EmptyPage:
        all_post = paginator.page(paginator.num_pages)

    return render(request, 'board/board.html', {'posts':all_post})


#게시판
def some_board(request, category_id):
    some_list = board.objects.all().filter(category_id=category_id)
    paginator = Paginator(some_list, 10)

    page = request.GET.get('page')
    try:
        some_post = paginator.page(page)
    except PageNotAnInteger:
        some_post = paginator.page(1)
    except EmptyPage:
        some_post = paginator.page(paginator.num_pages)

    return render(request, 'board/board.html', {'posts':some_post})

#후기게시판
def review(request):
    return render(request, 'board/review.html')

#후기게시글
def review_post(request):
    return render(request, 'board/review_post.html')

#일반게시글
def post(request):
    return render(request, 'board/post.html')

#글쓰기
def write(request):
    return render(request, 'board/write.html')

#내 페이지
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
