# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]