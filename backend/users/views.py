from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers

class RegisterRequest(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "success": True })
        return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
