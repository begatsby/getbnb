# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 23:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20160117_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='url',
        ),
    ]
