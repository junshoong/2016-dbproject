# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0007_auto_20161209_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=10),
        ),
    ]
