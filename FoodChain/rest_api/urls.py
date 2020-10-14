from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("available_food/", views.FoodAvailable.as_view(), name="Available Food"),
    path("food_request/", views.FoodRequest.as_view(), name="Available Food"),
    path("user_details/", views.Details.as_view(), name="Available Food")
]
