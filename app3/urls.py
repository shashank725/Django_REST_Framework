
from django.urls.conf import path, include
from app3 import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

## Register StudentViewSet with Router
# router.register('studentapi', views.studentViewSet, basename='student')
router.register('studentapi', views.studentModelViewSet, basename='student')
# router.register('studentapi', views.studentReadOnlyModelViewSet, basename='student')


app_name = 'app3'
urlpatterns = [
    path('', include(router.urls)),

]