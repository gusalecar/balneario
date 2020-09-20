from django.urls import include, path
from . import views
from .views import CarpaList


urlpatterns = [
    path('', views.TestRequest.as_view()),
    path('carpa/', CarpaList.as_view(), name ='carpa_list'),


]
