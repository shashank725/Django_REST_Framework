from django.db.models import manager
from django.shortcuts import render
from rest_framework import serializers

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.views import APIView

from .models import Student
# Create your views here.

# Class based Views
class studentApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def patch(self, request, pk=None, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        # serializer = StudentSerializer(instance=student, data=request.data)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk=None, format=None):
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg':'Data Deleted'})








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