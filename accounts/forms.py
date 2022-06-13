from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        models      =   CustomUser
        fields      =   UserCreationForm.Meta.fields+ ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models      =   CustomUser
        fields      =   UserChangeForm.Meta.fields