# for python 2
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class User(models.Model):
    login_id = models.CharField(max_length=11)
    pw = models.CharField(max_length=128)
    name = models.CharField(max_length=10)
    email = models.EmailField()
    period = models.IntegerField()
    position = models.CharField(max_length=15, default="일반회원")
    position_all = models.CharField(max_length=15, blank=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(blank=True)
    work = models.CharField(max_length=45, blank=True)
    work_phone = models.CharField(max_length=14, blank=True)
    work_position = models.CharField(max_length=45, blank=True)
    # open or not
    open_login_id = models.BooleanField()
    open_email = models.BooleanField()
    open_picture = models.BooleanField()
    open_work = models.BooleanField()
    open_work_phone = models.BooleanField()
    open_work_position = models.BooleanField()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
        ordering = ('-period',)

    def __str__(self):
        return self.name



