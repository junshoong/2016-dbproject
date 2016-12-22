from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+',
    )
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
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='+',
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "댓글"
        verbose_name = "댓글"
