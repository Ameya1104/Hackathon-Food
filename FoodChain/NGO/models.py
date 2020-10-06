from django.db import models
from django.contrib.auth.models import User


class Belongs(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="belong")
    is_ngo = models.BooleanField(default=False)
    is_donor = models.BooleanField(default = False)


