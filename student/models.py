
from django.db import models
from school.models import School
from user_and_role.models import User

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    studentId = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    realName = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    #user = models.ManyToManyField('User', blank=True)