from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Requis")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
