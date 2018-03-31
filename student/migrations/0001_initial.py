# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-31 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
                ('realName', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
    ]
