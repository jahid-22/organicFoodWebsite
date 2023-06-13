from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, UsernameField, password_validation, AuthenticationForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from . models import Customar

# User Registration Form


class UserRegi(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Email', 'username': 'User Name'}
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"})
        }

# User Login Form


class UserLogin(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": "form-control"})
    )

# Form for add Customar address


class CustomarAdd(forms.ModelForm):
    class Meta:
        model = Customar
        fields = ['name', 'email', 'phone', 'address', 'district']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'phone': forms.NumberInput(attrs={"class": "form-control"}),
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "থানা, ওয়ার্ড, গ্রাম"}),
            'district': forms.Select(attrs={"class": "form-control"}),
        }

# password change form


class MyPassChange(PasswordChangeForm):

    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password",
                   "autofocus": True, "class": "form-control"}
        ),
    )

    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "class": "form-control"}),
    )

# email form for password reset


class PassResetEmail(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={
                                "autocomplete": "email", "class": "form-control", "placeholder": "Your email"}),
    )

# password reset form


class PassReset(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "class": "form-control"}),
    )
