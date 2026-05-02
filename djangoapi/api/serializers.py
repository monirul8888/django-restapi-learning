from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=25)
    student_id = serializers.IntegerField()
    student_dept = serializers.CharField(max_length=15)


    def create(self, validated_data):
        return (Student.objects.create(**validated_data))
    
    def update(self, instance, validated_data):
        instance.student_name = validated_data.get("student_name", instance.student_name)
        instance.student_id = validated_data.get("student_id", instance.student_id)
        instance.student_dept = validated_data.get("student_dept", instance.student_dept)

        instance.save()
    

        return instance


