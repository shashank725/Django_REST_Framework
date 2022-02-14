
from django.urls.conf import path, include
from app3 import views
from rest_framework.routers import DefaultRouter

### For Token Authentication
## When want Token Authentication thorugh API endpoint withour creating auth.py file
# from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthToken

# Creating Router Object
router = DefaultRouter()

## Register StudentViewSet with Router
# router.register('studentapi', views.studentViewSet, basename='student')
router.register('studentapi', views.studentModelViewSet, basename='student')
# router.register('studentapi', views.studentReadOnlyModelViewSet, basename='student')


app_name = 'app3'
urlpatterns = [ 
    path('', include(router.urls)),

    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth')

]