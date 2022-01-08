from django.urls import path

from app2 import views
# from . import views

app_name = 'app2'
urlpatterns = [
    # path('hello/', views.hello, name='hello'),
    # path('studentapi/', views.studentApi, name='student-api'),   # Function based VIEW
    # path('studentapi/<int:pk>/', views.studentApi, name='student-api'),    # Function based VIEW
    # path('studentapi/', views.studentApi.as_view(), name='student-api'),    # Class based VIEW
    # path('studentapi/<int:pk>/', views.studentApi.as_view(), name='student-api'),    # Class based VIEW
    path('studentlist/', views.studentList.as_view(), name='student-list'),
    path('studentcreate/', views.studentCreate.as_view(), name='student-create'),
    path('studentretrive/<int:pk>/', views.studentRetrive.as_view(), name='student-retrive'),
    path('studentupdate/<int:pk>/', views.studentUpdate.as_view(), name='student-update'),
    path('studentdelete/<int:pk>/', views.studentDestroy.as_view(), name='student-delete'),
    
]