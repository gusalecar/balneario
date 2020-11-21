from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reservas', views.ReservaViewSet, 'reservas')
router.register(r'items', views.ItemViewSet, 'items')
router.register(r'transferencias', views.TransferenciaViewSet, 'transferencias')
router.register(r'precios', views.PrecioViewSet, 'precios')

urlpatterns = [
    path('', views.TestRequest.as_view()),
    path('auth/', include('backend.users.urls')),
    path('', include(router.urls)),
    path('pagos', views.PagoRequest.as_view())
]
