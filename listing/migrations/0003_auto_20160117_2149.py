# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20160111_2149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'amenities'},
        ),
        migrations.AlterModelOptions(
            name='propertyamenity',
            options={'verbose_name_plural': 'amenity'},
        ),
        migrations.AddField(
            model_name='photo',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
