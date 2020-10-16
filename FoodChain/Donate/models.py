from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


# Create your models here.
class FoodReq(models.Model):
    user = models.ForeignKey(User,related_name="foods",related_query_name="foods",blank=True,on_delete=models.CASCADE)
    foodtakenfrom=models.IntegerField(max_length=250,default=0)
    quantity_required=models.IntegerField(default=0)

class rate(models.Model):
    user = models.ForeignKey(User,related_name="foods11",related_query_name="foods11",blank=True,on_delete=models.CASCADE)
    fedto=models.IntegerField(default=0)
    ratings=models.PositiveIntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])


