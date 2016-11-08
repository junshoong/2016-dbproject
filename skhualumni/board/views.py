from django.shortcuts import render

# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list': post_list,})
