from django.urls import path

from app2 import views
# from . import views

app_name = 'app2'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('studentapi/', views.studentApi, name='student-api'),   # Function based VIEW
    path('studentapi/<int:pk>/', views.studentApi, name='student-api'),
    # path('student-api/', views.studentapi.as_view(), name='student-api'),    # Class based VIEW
    # path('student-create/', views.studentCreate, name='student-create'),
    # path('student-update/<str:pk>/', views.studentUpdate, name='student-update'),
    
]