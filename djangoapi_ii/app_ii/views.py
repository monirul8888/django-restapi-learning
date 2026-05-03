from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


def student_info (request):

    st = Student.objects.all()
    serializer = StudentSerializer(st, many= True)
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = "application/json")











