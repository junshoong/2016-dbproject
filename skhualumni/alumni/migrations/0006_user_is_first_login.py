# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_auto_20161130_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_first_login',
            field=models.BooleanField(default=True, verbose_name='최초로그인여부'),
        ),
    ]