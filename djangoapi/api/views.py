from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io

from rest_framework.parsers import JSONParser

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

@csrf_exempt
def student_insert(request):
    
    if request.method == "POST":
        json_data = request.body

        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)


        serializer = StudentSerializer(data = python_data)
        

        if serializer.is_valid():
            serializer.save()

            res = {"msg": "Successfully Inserted Data "}

            data = JSONRenderer().render(res)

            return HttpResponse( data, content_type = "application/json")
        
        data = JSONRenderer().render(serializer.errors)
        return HttpResponse( data, content_type = "application.json")


