from email.mime import multipart

import form as form
from django import forms
from django.forms import Form


class RegisterForm(Form):
    email = forms.EmailField(label='Your email', max_length=100)
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class PasswordChangeForm(Form):
    password_1 = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(widget=forms.PasswordInput())


class UploadFileForm(forms.Form):
    file = forms.FileField()
