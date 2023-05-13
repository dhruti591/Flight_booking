from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    Profile = models.ImageField(upload_to ='profile/')
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Balance = models.IntegerField(default=500)
    
    
    