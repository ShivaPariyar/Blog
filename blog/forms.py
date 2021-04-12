from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'photo', 'author']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'content': forms.Textarea(attrs={'class': 'form-control'}),
                   'author': forms.TextInput(attrs={'class': 'form-control'}),
                   }
        labels = {
            'title': 'Title',
            'content': 'Body',
            'photo': 'Photo',
            'author': 'Author',
        }


class Signup(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password (Again)'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        requireds = {'first_name': True, 'last_name': True, 'email': True}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }


class SignInForm(AuthenticationForm):
    username = forms.CharField(label_suffix=' ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label_suffix=' ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditProfile(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined']
        labels = {'email': 'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'last_login': forms.TextInput(attrs={'class': 'form-control'}),
            'date_joined': forms.TextInput(attrs={'class': 'form-control'}),
        }
