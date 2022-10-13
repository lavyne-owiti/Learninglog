
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Peaple(User):
    email= models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
