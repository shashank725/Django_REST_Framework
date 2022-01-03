from django.urls import path

from app import views
# from . import views

app_name = 'app'
urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('student-list/', views.studentList, name='student-list'),
    path('student-detail/<str:pk>/', views.studentDetail, name='student-detail')
]