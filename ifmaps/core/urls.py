from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalaViewSet, EventoViewSet

router = DefaultRouter()
router.register(r'salas', SalaViewSet)
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
