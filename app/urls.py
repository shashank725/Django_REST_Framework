from django.urls import path

from app import views
# from . import views

app_name = 'app'
urlpatterns = [
    path('apioverview', views.apiOverview, name='apiOverview'),
    path('student-list/', views.studentList, name='student-list'),
    # path('student-detail/<str:pk>/', views.studentDetail, name='student-detail'),
    path('student-api/', views.studentapi, name='student-api'),   # Function based VIEW
    # path('student-api/', views.studentapi.as_view(), name='student-api'),    # Class based VIEW
    path('student-create/', views.studentCreate, name='student-create'),
    # path('student-update/<str:pk>/', views.studentUpdate, name='student-update'),
    
]