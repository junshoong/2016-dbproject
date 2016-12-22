from django.db import models
from django.core.urlresolvers import reverse
from alumni.models import User
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=50)
    nt_writer = models.CharField(max_length=10,null=True)
    #writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    # nt_writer = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(max_length=10000)
    photo = models.ImageField(blank=True, null=True, upload_to='NoticeBoard/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "게시글"
        verbose_name = "게시글"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice:post_detail', args=(self.pk,))

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super(Post, self).delete(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    nt_author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "댓글"
        verbose_name = "댓글"
