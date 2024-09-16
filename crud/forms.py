from django.core import validators
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'example@gmail.com'}),
        }