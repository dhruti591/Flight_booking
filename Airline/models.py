from django.db import models
from django.db.models import Model

# Create your models here.
class Airline(models.Model):
    Airline_Id = models.IntegerField(primary_key=True)
    Airline_name = models.CharField(max_length=20)
    Airline_Photo = models.ImageField(upload_to ='media/')
    
    def __str__(self):
         return str(self.Airline_Id)
     
class Airline_manager(models.Model):
    Airline_username = models.CharField(primary_key=True,max_length=10)
    Airlien_password = models.CharField(max_length=10)
    Airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE)
    
    def __str__(self):
         return self.Airline_username
    
     


