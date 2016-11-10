# for python 2
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Info(models.Model):
    title = models.CharField(max_length=45)
    contents = models.TextField()
    image = models.ImageField(blank=True, upload_to='info/%Y')
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'info'
        db_table = 'other_board'

    def __str__(self):
        return self.title
