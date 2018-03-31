from django.contrib import admin
from django.db import models
from django import forms
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('school_id', 'course', 'workId', 'grade', 'realName', 'password', 'phone', 'nickName', 'description')

admin.site.register(Teacher, TeacherAdmin)