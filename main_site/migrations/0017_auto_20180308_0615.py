# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 22:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0016_auto_20180308_0605'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userInfo',
            new_name='userInfomation',
        ),
    ]
