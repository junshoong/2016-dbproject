# for python 2
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, login_id, name, birth, email, period, password=None, **kwargs):

        if not password:
            password = '0000'

        email = self.normalize_email(email),
        user = self.model(login_id, name, birth, email, period, **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_id, name, birth, email, period, password, **kwargs):
        user = self.create_user(login_id, name, birth, email, period, password, position='관리자', **kwargs)

        user.is_admin = True
        user.save(using=self._db)
        return user


@python_2_unicode_compatible
class User(AbstractBaseUser):

    login_id = models.CharField(max_length=11, unique=True)
    name = models.CharField(max_length=10)
    birth = models.DateField()
    email = models.EmailField()
    period = models.IntegerField()
    position = models.CharField(max_length=15, default="일반회원")
    position_all = models.CharField(max_length=15, blank=True)
    picture = models.ImageField(blank=True)
    work = models.CharField(max_length=45, blank=True)
    work_phone = models.CharField(max_length=14, blank=True)
    work_position = models.CharField(max_length=45, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # open or not
    open_login_id = models.BooleanField()
    open_email = models.BooleanField()
    open_picture = models.BooleanField()
    open_work = models.BooleanField()
    open_work_phone = models.BooleanField()
    open_work_position = models.BooleanField()

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = [
        'name',
        'birth',
        'email',
        'period',
    ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
        ordering = ('-period',)

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin




