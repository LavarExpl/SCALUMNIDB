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
        messages.success(request,"Your user has been created! You can go log in now!")
        return redirect('loginp')
    return render(request, "dbapp/register.html",{})

def loginp (request):
    if request.method =="POST":
         username= request.POST.get('Username')
         email= request.POST.get('Email')
         password= request.POST.get('Password')
         
         user = authenticate(username=username, email=email, password=password)
         if user is not None:
             # a backend authicated the credications 
              login(request,user)
              return redirect('/')
         else:
            messages.error(request , ' NO ACCOUNTS EXIST ')
            return redirect('register')
    
    return render(request, "dbapp/login.html",{})


def UserLoggedIn(request):
    
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def logout_v(request):
     username = UserLoggedIn(request)
     if username!= None:
          logout(request)
          return redirect('register')
def accounts (request):
 
        
    return render(request, "dbapp/accounts.html",{})
