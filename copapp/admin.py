# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import VictimCoordinates, FriendCoordinates, PoliceCoordinates, UserToken,UserInfo

admin.site.register(UserInfo)
admin.site.register(UserToken)
admin.site.register(FriendCoordinates)
admin.site.register(PoliceCoordinates)
admin.site.register(VictimCoordinates)

# Register your models here.
