import django


from django.urls import path
from .views import UserDetailsApi,RegisterUserAPIView

urlpattern =[
    path("get-details",UserDetailsApi.as_view()),
    path('register',RegisterUserAPIView.as_view()),
]