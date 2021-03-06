# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 01:07
from __future__ import unicode_literals

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20170430_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile',
            field=models.ImageField(default='default.png', upload_to=library.models.author_upload_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to=library.models.book_upload_path),
        ),
    ]
