# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-25 14:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0005_book_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='img',
        ),
    ]
