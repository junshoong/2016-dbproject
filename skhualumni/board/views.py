from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostEditForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'alumni/index.html', {
        'post_list': post_list,
    })

#포스트 보기
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'alumni/post_detail.html', {
        'post': post,
    })

#댓글 생성
def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('board:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'alumni/post_form.html', {
        'form': form,
    })

#댓글 수정
def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('board:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'alumni/post_form.html', {
        'form': form,
    })



def post_new(request):
    if request.method == "GET":
        edit_form = PostEditForm()
    elif request.method == "POST":
         edit_form = PostEditForm(request.POST, request.FILES)
         if edit_form.is_valid():
            post_new = edit_form.save()
            return redirect(post_new.get_absolute_url())

    return render(request, 'alumni/post_new.html', {
        'form': edit_form,
    })

