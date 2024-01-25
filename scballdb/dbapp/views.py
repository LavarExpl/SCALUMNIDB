from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

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
    return render(request, "dbapp/register.html",{})

def loginp (request):
   
        
    return render(request, "dbapp/login.html",{})

def accounts (request):
   
        
    return render(request, "dbapp/accounts.html",{})
