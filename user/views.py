from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
import re
from user.models import User_profile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def auth_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        # if validate_username(username):
        #     return render(request, 'register.html', {"error":"Username must be one Capital letter, more than two numbers"})
        
        user = User.objects.create_user( date_joined=timezone.now(),
                                        username=username,
                                        email=email,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()
        User_profile_object=User_profile(Username=user, Profile="custom_profile.jpg")
        User_profile_object.save()
        
        return render(request, 'home.html')
    else:
        print('not save')
        return render(request, 'register.html')
        
def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponsePermanentRedirect('/')
            # return render(request, 'home.html') 
        else:
            return render(request, 'login.html', {"error":"Your username or password is incorrect"})
    else:
        return render(request, 'login.html')
    
def auth_logout(request):
    logout(request)
    return HttpResponsePermanentRedirect('/')

def auth_profile(request):
    user = request.user
    print(user.username)
    profile = User_profile.objects.filter(Username = user).first().Profile
    
    return render(request, 'profile.html', {'user': user, "profile_pic": profile })

def change_profile(request, username):
    
    if request.method == 'POST': 
        user = request.user
        User_profile_object = User_profile.objects.filter(Username=user).first()
        
        uploaded_file = request.FILES['image']
        file_name = user.username + '.png' 
        file_path = default_storage.save(file_name, ContentFile(uploaded_file.read()))
        
        User_profile_object.Profile = file_path
        User_profile_object.save()
        
    return HttpResponsePermanentRedirect('/auth/profile')

def validate_username(username):
    # Check if the username contains at least one uppercase letter and more than two digits
    if not re.search(r'[A-Z]', username):
        return False
    if not re.findall(r'\d', username) or len(re.findall(r'\d', username)) <= 2:
        return False
    if len(username) <= 2:
        return False
    # If the username passes all validation checks, return True
    return True


