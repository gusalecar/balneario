from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reservas', views.ReservaViewSet, 'reservas')

urlpatterns = [
    path('', views.TestRequest.as_view()),
    path('auth/', include('backend.users.urls')),
    path('', include(router.urls))
]
