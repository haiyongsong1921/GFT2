from django.contrib import admin
from django.db import models
from django import forms
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('school_id', 'studentId', 'grade', 'realName', 'password', 'phone', 'description')


admin.site.register(Student, StudentAdmin)
