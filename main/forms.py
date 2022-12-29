from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class RegisterUserForm(UserCreationForm):  #класс формы регистрации
    class Meta:
        model = get_user_model()  #привязываем форму к модели
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')  #указываем нужные нам поля

class LoginUserForm(AuthenticationForm):  #класс формы логина
    username = forms.CharField(label='login', widget=forms.TextInput())
    password = forms.CharField(label='password', widget=forms.PasswordInput())