from django import forms
from .models import User

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput
        }


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput
        }