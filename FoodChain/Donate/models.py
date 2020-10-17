from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from NGO.models import foodAvbl

# Create your models here.
class FoodReq(models.Model):
    user = models.ForeignKey(User,related_name="foods",related_query_name="foods",blank=True,on_delete=models.CASCADE)
    foodtakenfrom=models.IntegerField(max_length=250,default=0)
    quantity_required=models.IntegerField(default=0)

class rate(models.Model):
    user = models.ForeignKey(User,related_name="foods11",related_query_name="foods11",blank=True,on_delete=models.CASCADE)
    fedto=models.IntegerField(default=0)
    ratings=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])

class orders(models.Model):
    O_ID=models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name="order_foods", related_query_name="order_foods", null=True, blank=True,
                             on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    pickup_address = models.TextField(max_length=20)
    s = models.IntegerField(default=1)


    



