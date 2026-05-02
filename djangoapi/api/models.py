from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=25)
    student_id = models.IntegerField()
    student_dept = models.CharField(max_length=15)


