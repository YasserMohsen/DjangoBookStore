# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20170430_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='died_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
