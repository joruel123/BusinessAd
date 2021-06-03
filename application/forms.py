from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')

class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username', max_length=150)
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput())