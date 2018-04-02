from django.db import models
from school.models import School
from student.models import Student
from user_and_role.models import User


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset()

    def query_by_column(self, column_id):
        query = self.get_queryset().filter(column_id=column_id)
        return query

    def query_by_school(self, school_id):
        # school = School.objects.get(id=school_id)
        teacher_list = self.get_queryset().filter(school_id=school_id)
        return teacher_list


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    course = models.CharField(max_length=20)
    workId = models.CharField(max_length=20)
    grade = models.CharField(max_length=20)
    realName = models.CharField(max_length=20)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    nickName = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    description = models.TextField()
    student = models.ManyToManyField(Student)
    # user = models.ManyToManyField('User', blank=True)

    objects = TeacherManager()

