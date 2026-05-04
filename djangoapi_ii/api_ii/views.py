from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.decorators import api_view

from rest_framework.response import Response

@api_view(["GET", "POST", "PUT", "PATCH"])
def insert(request, pk=None):
    if request.method == "GET":

        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)

            return Response(serializer.data)
        
        student = Student.objects.all()
        serializer = StudentSerializer(student, many= True)

        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"msg" : "Data Inserted Successfully"})
        return Response(serializer.errors)
    

    if request.method == "PUT":
        id = pk

        st_id = Student.objects.get(pk=id)

        serializer = StudentSerializer(st_id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "Data Updated Successfully"})
        
        return Response(serializer.errors)
            
    if request.method == "PATCH":
        id = pk

        st_id = Student.objects.get(pk=id)

        serializer = StudentSerializer(st_id, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg" : "Partial Data Updated Successfully"})
        
        return Response(serializer.errors)
            





