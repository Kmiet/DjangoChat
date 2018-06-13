from django import forms
from django.core.validators import validate_email

from .models import User

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput({'placeholder': 'Email', 'autocomplete': 'off', 'class': 'auth_field'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password', 'class': 'auth_field'}))

class RegisterForm(forms.Form):
    # nickname IS username
    username = forms.CharField(label= 'Nick', widget=forms.TextInput({'placeholder': 'Nick', 'autocomplete': 'off', 'class': 'auth_field'}))
    email = forms.EmailField(widget=forms.EmailInput({'placeholder': 'Email', 'autocomplete': 'off', 'class': 'auth_field'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'Password', 'autocomplete': 'off', 'class': 'auth_field'}))
    password_confirmation = forms.CharField(label='Confirm password', widget=forms.PasswordInput({'placeholder': 'Confirm password', 'autocomplete': 'off', 'class': 'auth_field'}))

    def clean_username(self):
        username = self.cleaned_data.get('username').capitalize();
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is not available")
        elif len(username) < 4:
            raise forms.ValidationError("Username must be at least 4 characters long")
        elif len(username) > 16:
            raise forms.ValidationError("Username must be 16 characters long or shorter")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already been taken")
        else:
            validate_email(email)

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        has_upper = 'xd'
        has_number = 'xd'
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        elif not has_upper:
            raise forms.ValidationError("Password must have at least one upper case letter")
        elif not has_number:
            raise forms.ValidationError("Password must have at least one digit")

        return password


    def clean(self):
        password = self.cleaned_data.get('password')
        password_c = self.cleaned_data.get('password_confirmation')
        if password_c != password:
            raise forms.ValidationError("Passwords does not match.")
        return self.cleaned_data