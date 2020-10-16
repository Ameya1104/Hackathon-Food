from django import forms
from Donate.models import FoodReq
from .models import rate
from django.contrib.auth.models import User

class FoodRequest(forms.ModelForm):
    class Meta:
        model=FoodReq
        fields = "__all__"
        exclude = ('user','foodtakenfrom',)

class Rate(forms.ModelForm):
    class Meta:
        model=rate
        fields = "__all__"
        widgets = {'ratings': forms.NumberInput(attrs={'class': 'Stars'})}
        labels = {'ratings': 'ratings /5'}
        exclude = ('user',)