from django.db import models
from django.core.urlresolvers import reverse
from alumni.models import User
#from django.contrib.auth.models import User

#class Categories(models.Model):

class Post(models.Model):
    #category = models.ForeignKey(Categories)
    title = models.CharField(max_length=50)
    #writer = models.ForeignKey(User, User.name, null=False)
    writer = models.ForeignKey(User)
    content = models.TextField(max_length=10000)
    photo = models.ImageField(blank=True, null=True, upload_to='NoticeBoard/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice:post_detail', args=(self.pk,))

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super(Post, self).delete(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

