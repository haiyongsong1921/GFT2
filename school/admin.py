from django.contrib import admin
from django.db import models
from django import forms
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('country', 'province', 'city', 'district', 'name', 'description')


admin.site.register(School, SchoolAdmin)
