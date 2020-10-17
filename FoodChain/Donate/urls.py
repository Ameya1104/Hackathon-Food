"""FoodChain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('login',views.login_u,name="login_u"),
    path('logout',views.logout_u,name="logout_u"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('loginpage/<int:id>',views.displaypage,name="displaypage"),
    path('loginpage/<int:id>/status/1',views.status1,name="status1"),
    path('loginpage/<int:id>/status/2',views.status2,name="status2"),
    path('loginpage/<int:id>/status/3',views.status3,name="status3"), 
    path('loginpage/<int:id>/status/4',views.status4,name="status4")   
]