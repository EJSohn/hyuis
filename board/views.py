# -*- coding: utf-8  -*-
from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from authen.models import hyu_users
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import board, comment, imghandler, category
from datetime import datetime
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

# Create your views here.

#전체게시판
def entire_board(request):
    today = datetime.today().date()
    all_list = board.objects.all().order_by('-post_id')
    paginator = Paginator(all_list, 10)

    page = request.GET.get('page')
    try:
        all_post = paginator.page(page)
    except PageNotAnInteger:
        all_post = paginator.page(1)
    except EmptyPage:
        all_post = paginator.page(paginator.num_pages)

    return render(request, 'board/board.html', {'posts':all_post, 'category':'전체', 'today':today})


#게시판
def some_board(request, category_id):
    today = datetime.today().date()
    some_list = board.objects.all().filter(category_id=category_id).order_by('-post_id')
    current_category = category.objects.get(category_id=category_id).category_name
    current_category_id=category.objects.get(category_id=category_id).category_id
    paginator = Paginator(some_list, 10)

    page = request.GET.get('page')
    request.session['current_page'] = page
    try:
        some_post = paginator.page(page)
    except PageNotAnInteger:
        some_post = paginator.page(1)
    except EmptyPage:
        some_post = paginator.page(paginator.num_pages)

    return render(request, 'board/board.html', {'posts':some_post, 'category':current_category, 'categoryid':current_category_id, 'today':today})

#후기게시판
def review(request):
    review_list = imghandler.objects.all().order_by('-post_id')
    paginator = Paginator(review_list, 8)

    page = request.GET.get('page')
    try:
        review_list = paginator.page(page)
    except PageNotAnInteger:
        review_list = paginator.page(1)
    except EmptyPage:
        review_list = paginator.page(paginator.num_pages)

    return render(request, 'board/review.html', {'reviews':review_list})

#후기게시글
def review_post(request):
    return render(request, 'board/review_post.html')

#일반게시글
def post(request, post_id):
    post = board.objects.get(post_id=post_id)

    #category_id = post.category_id
    #some_list = board.objects.all().filter(category_id=category_id).order_by('-post_id')
    #some_real_list = some_list.values()

    '''
    index = 1
    for post in some_real_list:
        if post['post_id']==post_id :
            break
        else :
            index += 1

    current_page = (index/10) + 1
    paginator = Paginator(some_list, 10)

    some_post = paginator.page(current_page)
    '''

    comme = comment.objects.all().filter(board_id=post_id).filter(parent_id__isnull=True)
    return render(request, 'board/post.html', {'post':post})

#글쓰기
def write(request):
    category_id=request.GET['category_id']
    return render(request, 'board/write.html', {'category':category_id})

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

    #글 등록
    post = board(title=title, content=content, created_date=created_date)

    cate = category.objects.get(category_id=category_id)
    user = hyu_users.objects.get(user_id=user_id)
    post.category_id = cate
    post.user_id = user
    post.save()


    #글 속의 이미지 등록
    class ImageParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'img':
                return
            if not hasattr(self, 'result'):
                self.result = []
            for name, value in attrs:
                if name == 'src':
                    self.result.append(value)

    parser = ImageParser()
    try:
        parser.feed(content)
        resultSet = set(x for x in parser.result)

        for x in sorted(resultSet):
            img = imghandler(image_url=x)
            pst = board.objects.get(post_id=post.post_id)
            img.post_id = pst
            img.save()
    except AttributeError:
        pass


    return HttpResponseRedirect(reverse('board:entire_view'))


def commenting(request, post_id):
    today = datetime.today()
    created_date = today

    user_id = request.session['member']
    content = request.POST['content']


    comme = comment(content=content, created_date=created_date)

    user = hyu_users.objects.get(user_id=user_id)
    boar = board.objects.get(post_id=post_id)
    comme.user_id = user
    comme.board_id = boar

    comme.save()
    print('succeed')

    return HttpResponseRedirect(reverse('board:post', args=[post_id]))

def recomment(request):
    today = datetime.today()
    created_date = today

    user_id = request.session['member']
    content = request.POST['content']
    parent = request.POST['comment_id']

    comme = comment(content=content, created_date=created_date)

    user = hyu_users.objects.get(user_id=user_id)
    parent_comment = comment.objects.get(comment_id=parent)
    boar = parent_comment.board_id

    comme.user_id = user
    comme.board_id = boar
    comme.parent_id = parent_comment

    comme.save()
    return HttpResponseRedirect(reverse('board:post', args=[boar.post_id]))


def post_delete(request, post_id):
    boar = board.objects.get(post_id=post_id)
    category_id = boar.category_id.category_id
    category_name = boar.category_id.category_name
    boar.delete()

    try:
        page = request.session['current_page']
    except:
        page = 1

    return HttpResponseRedirect('/board/{0}/{1}/?page={2}'.format(category_name, category_id, page))

def comment_delete(request, post_id):
    comment_id = request.GET.get('comment_id')
    comm = comment.objects.get(comment_id=comment_id)

    comm.delete()

    return HttpResponseRedirect(reverse('board:post', args=[post_id]))

def comment_update(request, post_id):
    comment_id = request.GET.get('comment_id')
    content = request.POST['content']

    comm = comment.objects.get(comment_id=comment_id)
    comm.content = content

    comm.save()

    return HttpResponseRedirect(reverse('board:post', args=[post_id]))