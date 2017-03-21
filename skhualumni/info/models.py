# coding=utf-8
# for python 2
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Info(models.Model):
    INFO_CATEGORY = (
        ('OLD_GRT', '전 원장 인사말'),
        ('GRT', '현 원장 인사말'),
        ('BSN', '사업안내'),
        ('ORG', '조직안내'),
        ('MAP', '오시는길'),
        ('USE', '이용안내'),
    )
    category = models.CharField(max_length=7, choices=INFO_CATEGORY)
    title = models.CharField(max_length=45)
    contents = models.TextField()
    image = models.ImageField(blank=True, upload_to='info/%Y')
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '기관소개글'
        verbose_name_plural = '기관소개글'
        db_table = 'other_board'
        ordering = ('-modified_date',)

    def __str__(self):
        return self.title
