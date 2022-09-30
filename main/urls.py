from django.urls import path, include
from rest_framework import routers
from .views import CryptoViewSet

app_name = 'main'

router = routers.DefaultRouter()
router.register(r'crypto', CryptoViewSet)

urlpatterns = [
	path('api/crypto/', include(router.urls)),
]