from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from .models import Customer


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['image','phone']