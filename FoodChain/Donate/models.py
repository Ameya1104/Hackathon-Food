from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FoodReq(models.Model):
    user = models.ForeignKey(User,related_name="foods",related_query_name="foods",blank=True,on_delete=models.CASCADE)
    foodtakenfrom=models.IntegerField(max_length=250,default=0)
    quantity_required=models.IntegerField(default=0)
