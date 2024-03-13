"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from home.views import StudentModelViewSet
from home.views import StudentModelApiView, SignUpAPIView, LoginAPIView, StandardModelApiView

router = DefaultRouter()
router.register(r'yourmodels', StudentModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('Standard/', StandardModelApiView.as_view()),
    path('Students/', StudentModelApiView.as_view()),
    path('signup/', SignUpAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
