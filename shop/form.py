from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .models import User

from django import forms


#Register Form


class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create New Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Your Password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']


#Password Changing Form


class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Create New Password'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Conform Your Password'}))
    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']


