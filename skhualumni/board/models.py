from django.db import models
from django.core.urlresolvers import reverse_lazy

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    photo = models.ImageField(blank=True, null=True, upload_to='FreeBoard/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.id})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
