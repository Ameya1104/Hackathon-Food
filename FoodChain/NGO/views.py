from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Registerdetail
from django.contrib.auth import authenticate,login,logout
from .models import Belongs
def index(request):
    return render(request,'NGO/index.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists try with a new one !")
            return redirect('/NGO/signup')
        if(len(username)<2 or len(username)>20):
            messages.error(request,"Username doesnt match the requirements")
            return redirect('/NGO/signup')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('/NGO/signup')
        if(password!=password1):
            messages.error(request,"Both passwords dont match")
            return redirect('/NGO/signup')
        myuser=User.objects.create_user(username,email,password)
        belong = Belongs(user = myuser,is_ngo =  True)
        belong.save()
        myuser.save()
        form= Registerdetail(request.POST ,request.FILES)
        if form.is_valid():
                object = form.save(commit=False)
                object.user = myuser
                object.save()

        
        messages.success(request,"Your NGO account has been successfully created")
        return redirect("/NGO")
        
    else:
        form = Registerdetail()
        return render(request,'NGO/signup.html',{"form":form})

def login_u(request):
    return render(request,'NGO/login.html')
    
def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/NGO")



def loginpage(request):
    if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            if Belongs.objects.get(user = user).is_ngo:
                login(request,user)
                messages.success(request,"Successfully Logged in")
                return render(request,'NGO/loginpage.html')
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'NGO/login.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'NGO/login.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'NGO/login.html')