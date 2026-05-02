from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer

# Create your views here.

def Student_views(request):

    st = Student.objects.all()

    serializer = StudentSerializer(st, many= True)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = "application/json")



def Student_view(request, pk):

    st = Student.objects.get(id = pk )

    serializer = StudentSerializer(st)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type = "application/json")

