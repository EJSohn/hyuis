from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.

def board(request):
    return HttpResponse('board entire view')

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
