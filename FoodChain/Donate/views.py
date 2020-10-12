from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from NGO.models import Belongs,foodAvbl,otherDetails,Cities
from NGO.forms import Registerdetail,otherDetails,foodAvbl
from .forms import FoodRequest
from .models import FoodReq




def index(request):
    return render(request,'Donate/index.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists try with a new one !")
            return redirect('signup')
        if(len(username)<2 or len(username)>20):
            messages.error(request,"Username doesnt match the requirements")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('signup')
        if(password!=password1):
            messages.error(request,"Both passwords dont match")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,password)
        belong = Belongs(user=myuser,is_donor =  True)
        belong.save()
        myuser.save()
        form= Registerdetail(request.POST ,request.FILES)
        if form.is_valid():
                object = form.save(commit=False)
                object.user = myuser
                object.save()
        
        messages.success(request,"Your account has been successfully created")
        return redirect("/Donate")
        
    else:
        form = Registerdetail()
        return render(request,'Donate/signup.html',{"form":form})

def login_u(request):
    return render(request,'Donate/login.html')
    
def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/Donate")



def loginpage(request):
    if request.method=="POST":
        #s=foodAvbl.objects.get(city=request.user.city)
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            if Belongs.objects.get(user = user).is_donor:
                login(request,user)
                details=otherDetails.objects.filter(user=request.user).values_list('city')
                for d in details:
                    s=Cities.objects.get(pk=d[0])
                j=foodAvbl.objects.filter(city=s)
                parameter={'j':j}
                messages.success(request,"Successfully Logged in")
                return render(request,'Donate/loginpage.html',parameter)
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'Donate/login.html')

        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'Donate/login.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'Donate/login.html')

def displaypage(request,id):
    if(request.method=="POST"):
        form=FoodRequest()
        m=id
        y=foodAvbl.objects.filter(id=id).values_list("quantity")
        h=foodAvbl.objects.get(id=id)
        form= FoodRequest(request.POST ,request.FILES)
        if(int(form['quantity_required'].value())>int(y[0][0])):
            print("HIIIIIIIIIIIIIIIIII")
            messages.error(request,"Cant be greater than available food")
            form = FoodRequest()
            y=foodAvbl.objects.filter(id=id)
            return render(request,'Donate/thankyou.html',{'form':form,'y':y})
        elif(int(form['quantity_required'].value())<int(y[0][0])):
            if form.is_valid():
                object = form.save(commit=False)
                object.user = request.user
                object.save()
                object.foodtakenfrom=m
                object.save()
                u=int(y[0][0])-int(form['quantity_required'].value())
                print(u)
                h.quantity=u
                h.save()
                messages.success(request,"Response Noted")
                return redirect ("/Donate/loginpage")
        
        else:
            messages.success(request,"Form invalid")
            return redirect("/Donate/loginpage")
        
    else:
        form = FoodRequest()
        y=foodAvbl.objects.filter(id=id)
        print(y)
        return render(request,'Donate/thankyou.html',{'form':form,'y':y})
        
