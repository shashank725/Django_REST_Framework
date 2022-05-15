from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'reuest': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

# # # Ways to Geaerate Token
# # Using Admin Application
# # Using Django manage.py command
  # python manage.py command drf_create_token <username> : This command will return API Token for the user or Create a Token if tpken doesn't exist.
# # By exposing an API endpoint (can be done withour creating auth.py)
  # pip install httpie
  # http POST http://127.0.0.1:8000/api-token-auth/ username="admin" password="admin"