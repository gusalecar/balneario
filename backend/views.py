from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail


class TestRequest(APIView):
    def get(self, request):
        return Response({
            "test": "data"
        })


class EmailRequest(APIView):
    def post(self, request):
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            # [request.user.email],
            ['from@example.com'],
            fail_silently=False,
        )
        return Response({
            "test": "data"
        })