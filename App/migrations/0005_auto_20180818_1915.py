# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-18 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_axf_foodtypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axf_foodtypes',
            name='childtypenames',
            field=models.CharField(max_length=200),
        ),
    ]