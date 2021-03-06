# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 16:25
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('born_at', models.DateField()),
                ('died_at', models.DateField()),
                ('contact', models.CharField(max_length=100)),
                ('rating', models.FloatField(default=0.0, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('published_at', models.DateField()),
                ('summary', models.CharField(max_length=1000)),
                ('country', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=20)),
                ('pages', models.IntegerField()),
                ('cover', models.CharField(max_length=100)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User_Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('r', 'read'), ('t', 'to be read'), ('c', 'currently reading'), ('n', 'nothing')], default='n', max_length=1)),
                ('rating', models.FloatField(default=0.0, validators=[django.core.validators.MaxValueValidator(5.0), django.core.validators.MinValueValidator(0.0)])),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(through='library.User_Book', to=settings.AUTH_USER_MODEL),
        ),
    ]
