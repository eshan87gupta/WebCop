# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copapp', '0002_auto_20180622_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
