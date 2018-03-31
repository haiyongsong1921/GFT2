from django.db import models

class School(models.Model):
    country = models.CharField(max_length=20, default='China')
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField()