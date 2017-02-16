# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('date', models.DateTimeField(verbose_name='date')),
                ('tag', models.CharField(default='', max_length=50)),
                ('link', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='')),
                ('size', models.CharField(default='', max_length=10)),
            ],
        ),
    ]