# for python 2
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,
    PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, login_id, name, period, password=None):
        if not login_id:
            raise ValueError('Users must have a login_id')

        user = self.model(
            login_id=login_id,
            name=name,
            period=period,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_id, name, period, password):
        u = self.create_user(login_id=login_id,
                             name=name,
                             period=period,
                             password=password,
                             )
        u.is_admin = True
        u.save(using=self._db)
        return u


@python_2_unicode_compatible
class User(AbstractBaseUser, PermissionsMixin):
    login_id = models.CharField('ID', max_length=11, unique=True)
    name = models.CharField('이름', max_length=10, blank=False)
    email = models.EmailField('Email', max_length=255, unique=True)
    birth = models.DateField('생일', null=True)
    period = models.IntegerField('기수', blank=True, default=0)
    position = models.CharField('동문회 직책', max_length=15, default="일반회원")
    position_all = models.CharField('총 동문회 직책', max_length=15, blank=True)
    picture = models.ImageField('프로필 사진', blank=True)
    work = models.CharField('직장', max_length=45, blank=True)
    work_phone = models.CharField('직장 전화', max_length=14, blank=True)
    work_position = models.CharField('직장 직위', max_length=45, blank=True)
    create_date = models.DateTimeField('가입일', auto_now_add=True)
    last_login = models.DateTimeField('마지막 로그인', auto_now=True, blank=True)
    is_active = models.BooleanField('사용여부', default=True)
    is_admin = models.BooleanField('관리자', default=False)
    # open or not
    open_login_id = models.BooleanField('핸드폰 번호 공개여부', default=False)
    open_email = models.BooleanField('이메일 공개여부', default=False)
    open_picture = models.BooleanField('프로필 사진 공개여부', default=False)
    open_work = models.BooleanField('직장 공개여부', default=False)
    open_work_phone = models.BooleanField('직장 전화 공개여부', default=False)
    open_work_position = models.BooleanField('직장 직위 공개여부', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = ['name', 'period']

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
