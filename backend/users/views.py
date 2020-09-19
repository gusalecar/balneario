from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response

class RegisterRequest(APIView):
    def post(self, request):
        data = request.data
        User.objects.create_user(
            data['username'],
            data['email'],
            data['password']
        )
        if authenticate(username = data['username'], password = data['password']) is not None:
            return Response({ "success": True })
        else:
            return Response({ "success": False })
