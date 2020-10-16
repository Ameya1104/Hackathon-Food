from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from NGO.models import Belongs,foodAvbl,otherDetails,Cities
from NGO.forms import Registerdetail,otherDetails,foodAvbl
from .forms import FoodRequest,Rate
from .models import FoodReq,rate, orders
from django.core.mail import send_mail


def Email(username,email):
    send_mail(
        subject = "alert",
        message = f'thanks {username} for joining us. Your account has been successfully created login for more details',
        from_email = "samvegvshah13@gmail.com",
        recipient_list = [email],
        fail_silently = False,
    )
def send(username,email,quantity):
    send_mail(
        subject = "alert",
        message = f'thanks {username} for the food you provided. {quantity} number of people have been fed !',
        from_email = "samvegvshah13@gmail.com",
        recipient_list = [email],
        fail_silently = False,

    )
def mailtoo(email,username):
    send_mail(
        subject = "alert",
        message = f'NGO {username} will come to collect the food order has been confirmed',
        from_email = "samvegvshah13@gmail.com",
        recipient_list = [email],
        fail_silently = False,
    )

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
        if(password!=password1):
            messages.error(request,"Both passwords dont match")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,password)
        belong = Belongs(user=myuser,is_donor =  True)
        belong.save()
        myuser.save()
        Email(username,email)
        form= Registerdetail(request.POST ,request.FILES)
        if form.is_valid():
                object = form.save(commit=False)
                object.user = myuser
                object.save()
        
        messages.success(request,"Your account has been successfully created")
        return redirect("/Donate/login")
        
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
    if request.user.is_authenticated:
        details=otherDetails.objects.filter(user=request.user).values_list('city')
        for d in details:
            s=Cities.objects.get(pk=d[0])
        j=foodAvbl.objects.filter(city=s)
        h=orders.objects.all()
        print(h)
        parameter={'j':j,'h':h}
        messages.success(request,"Successfully Logged in")
        return render(request,'Donate/loginpage.html',parameter)
    else:
        messages.success(request, "You need to login to access this")
        return render(request, 'Donate/login.html')

def displaypage(request,id):
    form = FoodRequest()
    y=foodAvbl.objects.filter(id=id)
    print(y)    
    return render(request,'Donate/thankyou.html',{'form':form,'y':y})

def status1(request,id):
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
                a=orders(O_ID=id,user=h.user,quantity=int(form['quantity_required'].value()),pickup_address=h.pickup_address)
                a.save()
                print(a)
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
                y=foodAvbl.objects.filter(id=id)
                y1=foodAvbl.objects.get(id=id) 
                parameter={'y':y,'y1':y1}
                return render(request,"Donate/status1.html",parameter)   
        else:
            messages.success(request,"Form invalid")
            return render(request,"/Donate/thankyou.html")    
    return render(request,"Donate/status1.html")

# def feedback(request,id):
#     if(request.method=="POST"):
#         print("Hi")
#         print("%%%%%%%%%%")
#         y=foodAvbl.objects.get(id=id)
#         email=y.user.email
#         form= Rate(request.POST ,request.FILES)
#         if form.is_valid():
#             object = form.save(commit=False)
#             quantity= form.instance.fedto
#             object.user=y.user
#             object.save()
#             send(y.user.username,email,quantity)
#             return HttpResponse("Well Done !")
#         else:
#             return HttpResponse("Bad Work")    
#     else:
#         form = Rate()
#         y=foodAvbl.objects.filter(id=id) 
#         return render(request,"Donate/rate.html",{'form':form,'y':y})

    
def status2(request,id):
    y=foodAvbl.objects.filter(id=id)
    y1=foodAvbl.objects.get(id=id) 
    parameter={'y':y,'y1':y1}
    if(request.method=="POST"):
        email=y1.user.email
        username=request.user
        mailtoo(email,username)        
        return render(request,"Donate/status2.html",parameter)
    else:
        return render(request,"Donate/status2.html",parameter)

def status3(request,id):
    y=foodAvbl.objects.filter(id=id)
    y1=foodAvbl.objects.get(id=id) 
    parameter={'y':y,'y1':y1}
    if(request.method=="POST"):       
        return render(request,"Donate/status3.html",parameter)
    return render(request,"Donate/status3.html",parameter)
    
def status4(request,id):
    y=foodAvbl.objects.filter(id=id)
    y1=foodAvbl.objects.get(id=id) 
    parameter={'y':y,'y1':y1}
    if(request.method=="POST"):
        email=y1.user.email
        form = Rate(request.POST ,request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            quantity= form.instance.fedto
            object.user=y1.user
            object.save()
            send(y1.user.username,email,quantity)
            messages.success(request,"You have completed the campaign. GOOD WORK!")
            return render(request,"Donate/status4.html",parameter)
        else:
            messages.success(request,"You couldn't complete the campaign. TRY AGAIN!")
            return render(request,"Donate/status4.html",parameter)  
    else:
        form = Rate()
        y=foodAvbl.objects.filter(id=id) 
        return render(request,"Donate/rate.html",{'form':form,'y':y})