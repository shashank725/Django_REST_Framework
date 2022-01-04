from functools import partial
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from requests.api import delete
from rest_framework import serializers

from .serializers import StudentSerializer
# from app import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

from django.views.decorators.csrf import csrf_exempt  # For Function based VIEW
from django.utils.decorators import method_decorator  # For Class based VIEW

from django.views import View

from .models import Student

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/student-list',
        'Detail View' : '/student-detail/<str:pk>/',
        'Create' : '/student-create/',
        'Update' : '/student-update/<str:pk>/',
        'Delete' : '/student-delete/<str:pk>',
    }
    return Response(api_urls)


# @api_view(['GET'])
def studentList(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    # return Response(serializer.data)

# To render data into JSON which is understandable by Frontend
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')

# To render data into JSON which is understandable by Frontend using JsonResponse
    return JsonResponse(serializer.data, safe=False) #In order to allow non-dict objects to be serialized set the safe parameter to False (By default it is set to "True").


# @api_view(['GET'])
# def studentDetail(request, pk):
#     student = Student.objects.get(id=pk)
#     serializer = StudentSerializer(student, many=False)
#     return Response(serializer.data)




# To get secific/all tudent detail with Create and Update
# Function based VIEW
@csrf_exempt
def studentapi(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        student.delete()
        res = {'msg': 'Data Deleted !'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')

# # Class based VIEW
# @method_decorator(csrf_exempt, name='dispatch')
# class studentapi(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             student = Student.objects.get(id=id)
#             serializer = StudentSerializer(student)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type='application/json')
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')
#     def post(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         serializer = StudentSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Created'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#     def put(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         student = Student.objects.get(id=id)
#         serializer = StudentSerializer(student, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg': 'Data Updated'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type='application/json')
#         else:
#             json_data = JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data, content_type='application/json')
#     def delete(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         student = Student.objects.get(id=id)
#         student.delete()
#         res = {'msg': 'Data Deleted !'}
#         json_data = JSONRenderer().render(res)
#         return HttpResponse(json_data, content_type='application/json')


# Another way to entering Data
@csrf_exempt
def studentCreate(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)  
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

# Does same thing as above
# @api_view(['POST'])
# def studentCreate(request):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



# @api_view(['POST'])
# def studentUpdate(request, pk):
#     task = Student.objects.get(id=pk)
#     serializer = StudentSerializer(instance=task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def studentDelete(request, pk):
#     student = Student.objects.get(id=pk)
#     student.delete()
#     return Response('Item Deleted')