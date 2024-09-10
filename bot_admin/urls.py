from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include


router = DefaultRouter()
router.register('channels', ChannelViewSet)
router.register('movies', MovieViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
