"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from unicodedata import name
from django import views
from django.contrib import admin
from django.db import router
from django.urls import path,include
from rest_framework.authtoken import views 
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,)

router=DefaultRouter()
router.register(r'image',ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('',include('learning_logs.urls')),
    path('', include('api.urls')),
    path('api-token-auth',views.obtain_auth_token),

    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',include(router.urls)),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

