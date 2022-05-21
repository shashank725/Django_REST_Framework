from functools import partial
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.serializers import Serializer
# from app import serializers

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from .serializers import StudentSerializer
from .custompermissions import MyPermission
from .models import Student

# Token Authentication
from rest_framework.authentication import TokenAuthentication

# Custom Authentication
from .custom_auth import CustomAuthentication

# JWT Authentication
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class studentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [JWTAuthentication]
    # authentication_classes = [CustomAuthentication] # Using Custom Authentication
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [MyPermission]



class studentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# class studentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         print("*********List**********")    # Can be used in all other methods like retrieve, update etc
#         print("basename :", self.basename)
#         print("action :", self.action)
#         print("detail :", self.detail)
#         print("suffix :", self.suffix)
#         print("name :", self.name)
#         print("description :", self.description)
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
#     def retrieve(self, request, pk=None):
#         id=pk
#         if id is not None:
#             student = Student.objects.all()
#             serializer = StudentSerializer(student, many=True)
#             return Response(serializer.data)
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
#     def update(self, request, pk):
#         id=pk
#         student = Student.objects.get(pk=id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Complete Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def partial_update(self, request, pk):
#         id=pk
#         student = Student.objects.get(pk=id)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'Partial Data Updated'})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def destroy(self, request, pk):
#         id = pk
#         student = Student.objects.get(pk=id)
#         student.delete()
#         return Response({'msg':'Data Deleted'})
