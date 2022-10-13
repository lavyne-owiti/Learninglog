"""Defines URL patterns for users"""
from django.urls import path,include
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework_simplejwt import views as jwt_views

app_name='users'
urlpatterns=[
    # include default auth urls.
    path('',include('django.contrib.auth.urls')),
    #registration page.
    path('register/',views.register,name='register'),
    # path('api/token',jwt_views.TokenObtainPairView.as_view()),
    # path('api/token/refresh',jwt_views.TokenRefreshView.as_view()),
]

