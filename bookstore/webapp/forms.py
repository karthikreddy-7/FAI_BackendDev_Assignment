from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Record

# Register/create a user


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


# Login a User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# add a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["Book_name", "author", "ISBN", "price", "quantity"]


# update a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ["Book_name", "author", "ISBN", "price", "quantity"]
