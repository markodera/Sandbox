from .models import User, Task, Comment
from django import forms
from django.forms import ModelForm

#form for user
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first', 'last', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        