from django.shortcuts import render
from Flight.models import Flight, Airline
import math
import random

def manageflight(request, Airline_id):
    
    flight_objects = Flight.objects.filter(Airline_id=Airline_id)
    flight_list = []
    
    for i in flight_objects:    
        # find total time journey
        test_dist = i.Dist_bet_airports.split(",")
        routes_distance = [int(i) for i in test_dist]
        temp_duration = convert12(convert_time_to_time(sum(routes_distance)/115)).split(":")
        duration_time = str(temp_duration[0]) + \
                " Hour " + str(temp_duration[1]) + " minute"                
        # print(duration_time)
        
        # find route des 
        test_routes = i.Routes.split(",")
        rotes_des = test_routes[0] + " to " + test_routes[-1]
        # print(rotes_des)
        
        flight_list.append({"Capacity": i.Total_ticket,
                            "Duration": duration_time,
                            "route_des": rotes_des,
                            "flight_id": i.Flight_id})
        # print(flight_list)
        
    return render(request, 'manageflight.html', {"flights": flight_list, "Airline_id": Airline_id})

def updateflight(request, Flight_id):
    
    if request.method=="POST":
        Routes=request.POST['routes']
        Dist_bet_airports=request.POST['distance']
        Total_ticket=request.POST['total_tickets']
        Depart_time=convert_time_to_string(request.POST['depart_time'])
        Flight_object=Flight.objects.get(pk=Flight_id)
        
        Flight_object.Routes = Routes
        Flight_object.Dist_bet_airports = Dist_bet_airports
        Flight_object.Total_ticket = Total_ticket
        Flight_object.Depart_time = Depart_time

        Flight_object.save()
    
    flight_object = Flight.objects.get(pk=Flight_id)
    # print(flight_object.Routes)
    return render(request, 'updateflight.html', {'flight':flight_object})

def createflight(request, Airline_id):
    return render(request, 'addflight.html', {'Airline_id':Airline_id})

def sucessflight(request, Airline_id):
    n=5
    Flight_id = random.randrange(10**(n-1), 10**n)
    if request.method=="POST":
        Routes=request.POST['routes']
        Dist_bet_airports=request.POST['distance']
        Total_ticket=request.POST['total_tickets']
        Depart_time=convert_time_to_string(request.POST['depart_time'])
        
        Airline_object = Airline.objects.get(Airline_Id=Airline_id)
        Flight_object = Flight(Flight_id=Flight_id,Airline_id=Airline_object,Routes=Routes,Dist_bet_airports=Dist_bet_airports,Depart_time=Depart_time,Total_ticket=Total_ticket)
        Flight_object.save()

        return render(request, 'successflight.html', {'flight':Flight_object})
    
def convert_time_to_time(time):
     # 1.5 to 01:30:00 
    floor_hour = math.floor(time)
    hour = f'{floor_hour:02d}'
    min = f'{int(abs(time - floor_hour)*60):02d}'
    result = str(hour)+":"+str(min)+":00"
    return result

def convert_time_to_string(time):
    # 01:30:00 to 1.5
    hour = int(time.split(':')[0])
    minutes = int(time.split(':')[1])
    print(minutes/60)
    result = str(round(float(hour+(minutes/60)),2))
    # print(result)
    return result;

def convert12(str):
    ans = ""
    h1 = ord(str[0]) - ord('0')
    h2 = ord(str[1]) - ord('0')
    hh = h1 * 10 + h2
    Meridien = ""
    if (hh < 12):
        Meridien = "AM"
    else:
        Meridien = "PM"
    hh %= 12
    if (hh == 0):
        ans = ans + "12"
        for i in range(2, 8):
            ans = ans + str[i]
    else:
        ans = ans + "{}".format(hh)
        for i in range(2, 8):
            ans = ans + str[i]
    return ans + " " + Meridien

