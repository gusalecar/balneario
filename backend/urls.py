from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.TestRequest.as_view()),
    path('email/', views.EmailRequest.as_view()),
    path('auth/', include('backend.users.urls')),
]
