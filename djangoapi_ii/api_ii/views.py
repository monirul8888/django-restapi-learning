# from django.shortcuts import render
# from .models import *
# from .serializer import *

# from rest_framework.decorators import api_view

# from rest_framework.views import APIView

# from rest_framework.response import Response

# class StudentInsert(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)

#             return Response(serializer.data)
        
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many= True)

#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data = request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response({"msg" : "Data Inserted Successfully"})
#         return Response(serializer.errors)
    

#     def put(self, request, pk, format=None):
#         id = pk
#         st_id = Student.objects.get(pk=id)

#         serializer = StudentSerializer(st_id, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg" : "Data Updated Successfully"})
        
#         return Response(serializer.errors)
            
#     def patch(self, request, pk, format=None):
#         id = pk
#         st_id = Student.objects.get(pk=id)

#         serializer = StudentSerializer(st_id, data = request.data, partial = True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"msg" : "Partial Data Updated Successfully"})
        
#         return Response(serializer.errors)
    

#     def delete(self, request, pk, format=None):
#         id = pk
#         st_id = Student.objects.get(pk=id)

#         st_id.delete()

#         return Response({"msg" : "Data Deleted Successfully"})

            




from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    
)

class CRUD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentList(GenericAPIView,
                  ListModelMixin,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)