from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ["id", "student_name", "student_id", "student_dept"]
