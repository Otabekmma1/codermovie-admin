"""
URL configuration for coder_movie_bot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from . import settings
from rest_framework.routers import DefaultRouter
from bot_admin.views import *
from django.urls import path, include


router = DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
