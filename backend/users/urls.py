from django.urls import path, include

from . import views

urlpatterns = [
    path('register', views.RegisterRequest.as_view()),
    path('', include('drf_social_oauth2.urls', namespace='drf')),
]
