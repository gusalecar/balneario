from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.TestRequest.as_view()),
]