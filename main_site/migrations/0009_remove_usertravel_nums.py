# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0008_usertravel_nums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertravel',
            name='nums',
        ),
    ]
