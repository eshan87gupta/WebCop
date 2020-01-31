# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    phone_number = models.CharField(max_length=15, null=True)
    name = models.CharField(max_length=15, null=True)
    # friend_phone_number = models.CharField(max_length=15, null=True)
    role = models.CharField(max_length=50, null=True)
    objects = models.Manager()


class VictimCoordinates(models.Model):
    latitude = models.FloatField(max_length=20, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    objects = models.Manager()


class FriendCoordinates(models.Model):
    latitude = models.FloatField(max_length=20, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    objects = models.Manager()

class Notifications(models.Model):
    message = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    objects = models.Manager()


class PoliceCoordinates(models.Model):
    latitude = models.FloatField(max_length=20, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    objects = models.Manager()


class UserToken(models.Model):
    token = models.CharField(max_length=500, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    objects = models.Manager()