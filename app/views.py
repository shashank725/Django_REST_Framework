from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .serializers import StudentSerializer
# from app import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

from django.views.decorators.csrf import csrf_exempt

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


@api_view(['GET'])
def studentDetail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


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



# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return Response('Item Deleted')