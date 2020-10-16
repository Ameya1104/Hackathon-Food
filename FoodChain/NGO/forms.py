from django import forms
from NGO.models import otherDetails,foodAvbl
from django.contrib.auth.models import User

class Registerdetail(forms.ModelForm):
    class Meta:
        model=otherDetails
        fields = "__all__"
        exclude = ('user',)

class Food(forms.ModelForm):
    class Meta:
        date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
        model=foodAvbl
        fields = "__all__"
        exclude = ('user','otherDetails','city','created_on','images')