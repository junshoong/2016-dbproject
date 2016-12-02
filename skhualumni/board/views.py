from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import Post, Comment
from .forms import CommentForm, PostEditForm, PostSearchForm
from django.contrib.auth.decorators import login_required
rows_per_page = 2

@login_required
def index(request):
    post_list = Post.objects.all()
    return render(request, 'board/index.html', {
        'post_list': post_list,
    })


# 글 검색
class post_search(FormView):
    form_class = PostSearchForm
    template_name = 'board/post_search.html'

    def form_valid(self, form):
        sch_word = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=sch_word) |
                                        Q(content__icontains=sch_word)).distinct
        context = {'form': form, 'search_term': sch_word, 'object_list': post_list}
        return render(self.request, self.template_name, context)  # No Redirection


# 포스트 보기
@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'board/post_detail.html', {
        'post': post,
    })


# 글 수정
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostEditForm(instance=post)
    return render(request, 'board/post_new.html', {
        'form': form})


# 글 삭제
@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()

    return redirect('board:index')


# 새글 작성
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostEditForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostEditForm()
    return render(request, 'board/post_new.html', {'form': form})


# 댓글 생성
@login_required
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
    return render(request, 'board/post_form.html', {
        'form': form,
    })


# 댓글 수정
@login_required
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
    return render(request, 'board/post_form.html', {
        'form': form,
    })
