# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0005_auto_20180115_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('userSex', models.BooleanField(default=1)),
                ('creditLevel', models.IntegerField(default=0)),
            ],
        ),
    ]
