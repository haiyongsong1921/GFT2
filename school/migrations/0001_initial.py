# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-31 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='China', max_length=20)),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]