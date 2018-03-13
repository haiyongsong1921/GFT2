# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='L1Factor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('factor_type', models.CharField(choices=[('S', 'Shared'), ('P', 'Private')], default='S', max_length=1)),
                ('target_type', models.CharField(choices=[('I', 'Individual'), ('T', 'Team')], default='T', max_length=1)),
                ('owner', models.CharField(max_length=50)),
            ],
        ),
    ]
