from typing import Any
from django.forms.renderers import BaseRenderer
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms

# Create your views here.
@login_required
def home(request):
    return render(request, 'dbapp/home.html',{})


def register (request):
    if request.method == "POST":
        username =request.POST.get("username")
        email =request.POST.get("email")
      
        password =request.POST.get("passcode")
        if len(password)  <3 :
                 
                 if len(username)<3:
                    messages.error(request , 'Password and username should have at least 3 charecters')
                    return redirect('register')
        
        all_users =User.objects.filter(username=username)
        if all_users:
              messages.error(request , ' Error username is already taken!')
              return redirect('register')
        


        new_user = User.objects.create_user(username=username,password=password,email=email)
        new_user.save()

        print(f"this users name is {username} and his email is {email} and password was {password}.")
        messages.success(request,"Your user has been created! You can go log in now!")
        return redirect('loginp')
    return render(request, "dbapp/register.html",{})

 

def loginp(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username_or_email = request.POST.get('Username')
        password = request.POST.get('Password')

        # Assuming username_or_email can be either a username or an email
        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'NO ACCOUNTS EXIST')
            return redirect('register')

    return render(request, "dbapp/login.html", {})



def logout_ (request):
     logout(request)
     return redirect('loginp')
