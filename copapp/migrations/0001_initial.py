# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FriendCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=20, null=True)),
                ('longitude', models.FloatField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PoliceCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=20, null=True)),
                ('longitude', models.FloatField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('name', models.CharField(max_length=15, null=True)),
                ('friend_phone_number', models.CharField(max_length=15, null=True)),
                ('role', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VictimCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=20, null=True)),
                ('longitude', models.FloatField(max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
