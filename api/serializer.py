from dataclasses import fields
import email
import re
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from api.models import Peaple

#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peaple
        fields =["id","first_name","last_name","username"]

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,
    validators=[UniqueValidator(queryset=User.objects.all())])
    password =serializers.CharField(
        write_only=True,required=True, validators=[validate_password])
    password1 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model= User
        fields = ('username', 'password', 'password1',
         'email', 'first_name', 'last_name')
        extra_kwags ={
            'first_name':{'required':True},
            'last_name':{'required':True}
        }
    def validate(self,attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user