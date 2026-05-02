from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=25)
    student_id = serializers.IntegerField()
    student_dept = serializers.CharField(max_length=15)


    def create(self, validated_data):
        return (Student.objects.create(**validated_data))


