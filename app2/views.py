from django.db.models import manager
from django.shortcuts import render
from rest_framework import serializers

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Student
from .serializers import StudentSerializer
# Create your views here.

# Class based Views

class studentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class studentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class studentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer






# class studentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
# class studentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# # Above 2 views can also be written together since they does not require PK
# class LCstudentApi(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class studentRetrive(GenericAPIView, RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
# class studentUpdate(GenericAPIView, UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
# class studentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
# # Above 3 views can also be written together since they require PK
# class RUDstudentApi(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)







# class studentApi(APIView):
#     def get(self, request, pk=None, format=None):
#         id = pk
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         else:
#             student = Student.objects.all()
#             serializer = StudentSerializer(student, many=True)
#             return Response(serializer.data)
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def put(self, request, pk=None, format=None):
#         id = pk
#         student = Student.objects.get(pk=id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     def patch(self, request, pk=None, format=None):
#         id = pk
#         student = Student.objects.get(pk=id)
#         # serializer = StudentSerializer(instance=student, data=request.data)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     def delete(self, request, pk=None, format=None):
#         id = pk
#         student = Student.objects.get(pk=id)
#         student.delete()
#         return Response({'msg':'Data Deleted'})

















# # Function based Views
# @api_view(['GET','POST'])
# def hello(request):
#     if request.method == 'GET':
#         return Response({'msg':'GET Request'})
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg':'POST Request', 'data':request.data})
# 
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def studentApi(request, pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         else:
#             student = Student.objects.all()
#             serializer = StudentSerializer(student, many=True)
#             return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'PUT':
#         id = pk
#         student = Student.objects.get(pk=id)
#         serializer = StudentSerializer(student, data=request.data) #partial=True
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     if request.method == 'PATCH':
#         id = pk
#         student = Student.objects.get(pk=id)
#         # serializer = StudentSerializer(instance=student, data=request.data)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     if request.method == 'DELETE':
#         id = pk
#         student = Student.objects.get(pk=id)
#         student.delete()
#         return Response(serializer.data)