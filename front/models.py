from django.db import models
from rest_framework import serializers

# Create your models here.
class Project(models.Model):
    idChiste=models.CharField(max_length=200)
    value= models.TextField()
    url= models.CharField(max_length=150)
    user= models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    