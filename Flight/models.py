from Airline.models import Airline
from django.db import models

class Flight(models.Model):
    Flight_id = models.IntegerField(primary_key=True)
    Airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE) 
    Routes = models.CharField(max_length=500)
    Dist_bet_airports= models.CharField(max_length=500)
    Depart_time = models.CharField(max_length=100)
    Total_ticket = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.Flight_id)
    
class Flight_component(models.Model):
    Sr_no = models.IntegerField(default=0)
    Temparal_ID = models.CharField(primary_key=True, max_length=1000)
    Flight_Id = models.IntegerField(default=12)
    Airline_logo = models.ImageField(upload_to ='media/')
    Airline_name = models.CharField(max_length=100, default="airline")
    Flightname1 = models.CharField(max_length=100)
    Flightname2 = models.CharField(max_length=100)
    Timeduration = models.CharField(max_length=100)
    Price = models.IntegerField(default=0)
    Total_ticket = models.IntegerField(default=0)
    Depart_time = models.CharField(max_length=100,default='SOME STRING')
    Arrive_time = models.CharField(max_length=100,default='SOME STRING')
    
    def __str__(self):
        str = self.Flightname1 + " to "+ self.Flightname2
        return str
    
    
    
    
