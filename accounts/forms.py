from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    firstname = forms.CharField(
        max_length=100, required=False, initial='Optional......')
    lastname = forms.CharField(
        max_length=100, required=False, initial='Optional......')
    email = forms.EmailField(required=True, help_text='Required')

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username',
                  'email', 'password1', 'password2']
