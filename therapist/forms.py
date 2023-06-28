from django import forms
from django.contrib.auth.models import User
from . import models

class TherapistUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class TherapistForm(forms.ModelForm):
    class Meta:
        model=models.Therapist
        fields=['address','mobile','profile_pic']

