from django.shortcuts import render
from .models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, 'alumni/index.html', {
        'post_list': post_list,
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'alumni/post_detail.html', {
        'post': post,
    })


def post_new(request):
    return render(request, 'alumni/post_form.html')
