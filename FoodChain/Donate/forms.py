from django import forms
from Donate.models import FoodReq
from django.contrib.auth.models import User

class FoodRequest(forms.ModelForm):
    class Meta:
        model=FoodReq
        fields = "__all__"
        exclude = ('user','foodtakenfrom',)