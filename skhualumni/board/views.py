from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import Post, Comment
from .forms import CommentForm, PostEditForm, PostSearchForm



def index(request):
    post_list = Post.objects.all()
    return render(request, 'alumni/index.html', {
        'post_list': post_list,
    })

# 글 검색
class post_search(FormView):
    form_class = PostSearchForm
    template_name = 'alumni/post_search.html'

    def form_valid(self, form):
        sch__Word = '%s' % self.request.POST['search_word']
        post_list = [Post.objects.filter(Q(title__icontains=sch__Word) |
                                         Q(description__icontains=sch__Word) | Q(
            content__icontains=sch__Word)).distinct]
        # post_list = Post.objects.filter(Q(title__icontains=sch__Word) |
        #                                 Q(description__icontains=sch__Word) | Q(content__icontains=sch__Word)).distinct()
        context = {'form': form, 'search_term': sch__Word, 'object_list': post_list}
        return render(self.request, self.template_name, context) #No Redirection


# 포스트 보기
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'alumni/post_detail.html', {
        'post': post,
    })


# 글 수정
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
    return render(request, 'alumni/post_new.html', {
        'form': form})


# 새글 작성
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
    return render(request, 'alumni/post_new.html', {'form': form})


# 댓글 생성
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

# 댓글 수정
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
