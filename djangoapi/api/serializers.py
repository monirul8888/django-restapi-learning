from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    student_name = serializers.CharField(max_length=25)
    student_id = serializers.IntegerField()
    student_dept = serializers.CharField(max_length=15)

    