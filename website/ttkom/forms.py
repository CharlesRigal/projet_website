from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Comment

class ChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Requis")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content": "commentaire"
        }