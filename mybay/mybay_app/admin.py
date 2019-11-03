# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AppUser, AppItem

# Register your models here.
admin.site.register(AppUser)
admin.site.register(AppItem)