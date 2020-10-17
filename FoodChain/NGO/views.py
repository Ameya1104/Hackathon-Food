from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from bootstrap_datepicker_plus import DateTimePickerInput
from .forms import Registerdetail, Food
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout
from .models import Belongs, foodAvbl, otherDetails,TypeOf,Cities,Measurement,History
from django.core.mail import send_mail
from django.utils import timezone


def index(request):
    return render(request, 'NGO/index.html')

def Email(username,email):
    send_mail(
        subject = "alert",
        message = f'thanks {username} for joining us. Your account has been successfully created login for more details',
        from_email = "samvegvshah13@gmail.com",
        recipient_list = [email],
        fail_silently = False,
    )


def signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists try with a new one !")
            return redirect('/NGO/signup')
        if (len(username) < 2 or len(username) > 20):
            messages.error(request, "Username doesnt match the requirements")
            return redirect('/NGO/signup')
        if (password != password1):
            messages.error(request, "Both passwords dont match")
            return redirect('/NGO/signup')
        myuser = User.objects.create_user(username, email, password)
        belong = Belongs(user=myuser, is_ngo=True)
        belong.save()
        myuser.save()
        Email(username,email)
        form = Registerdetail(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = myuser
            object.save()

        messages.success(request, "Your NGO account has been successfully created")
        return redirect("/NGO/login")

    else:
        form = Registerdetail()
        return render(request, 'NGO/signup.html', {"form": form})


def login_u(request):
    return render(request, 'NGO/login.html')


def logout_u(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect("/NGO")


def loginpage(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            if Belongs.objects.get(user=user).is_ngo:
                login(request, user)
                messages.success(request, "Successfully Logged in")
                form = Food()
                return render(request, 'NGO/loginpage.html', {"form": form})
            else:
                messages.error(request, "Wrong credentials,Please try again !")
                return render(request, 'NGO/login.html')
        else:
            messages.error(request, "Wrong credentials,Please try again !")
            return render(request, 'NGO/login.html')
    if request.user.is_authenticated:
        print(request.user)
        form = Food()
        return render(request, 'NGO/loginpage.html', {"form": form})
    else:
        messages.success(request, "You need to login to access this")
        return render(request, 'NGO/login.html')
        


def check_user(user):
    return Belongs.objects.get(user=user).is_ngo


@login_required
def availability(request):
    if request.method == "POST":
        m = otherDetails.objects.get(user=request.user)
        form = Food(request.POST, request.FILES)
        s=str(m.city)
        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()
            object.city = s
            object.save()
            object.images=m.image
            object.save()
            object.created_on=timezone.now()
            object.save()
            messages.success(request, "Thankyou for the food alert")
            return redirect("/NGO/loginpage")
            
        else:
            return redirect("/NGO/loginpage")
    else:
        return redirect("/NGO/loginpage")

def alerts(request):
    if(History.objects.filter(user=request.user) is not None ):
        j = History.objects.filter(user=request.user)
        parameter={'j':j}
        return render(request, 'NGO/alert.html',parameter)
    else:
        return HttpResponse("No alerts till date")