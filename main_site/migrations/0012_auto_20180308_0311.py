# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0011_auto_20180308_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
