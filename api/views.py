
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# Create your views here.
# Class based view to Get User Details using Token Authentication

class UserDetailsApi(APIView):
    authentication_classes =(TokenAuthentication,)
    permission_classes =(AllowAny,)
    def get (self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer= UserSerializer(user)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes= (AllowAny,)
    serializer_class =RegisterSerializer