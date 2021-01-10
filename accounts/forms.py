from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order, Customer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"

        widgets = {
            "customer": forms.TextInput(attrs={
                "class": "validate",
                "id": "customer",
                "type": "text"
            }),
            "product": forms.TextInput(attrs={
                "class": "validate",
                "id": "product",
                "type": "text"
            }),
            "status": forms.Select(attrs={
                "class": "validate",
                "id": "status",
                "type": "text"
            }),
            "delete": forms.CheckboxInput(attrs={
                "id": "delete",
                "type": "radio"
            })
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "validate",
                "id": "name",
                "type": "text"
            }),
            "phone": forms.TextInput(attrs={
                "class": "validate",
                "id": "phone",
                "type": "text",
                "placeholder": "Add country code + areacode ej. +013334445555"
            }),
            "email": forms.EmailInput(attrs={
                "class": "validate",
                "id": "email",
                "type": "email"
            })
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "validate",
                "id": "username",
                "type": "text",
                "placeholder": "Enter Username"
            }),
            "email": forms.EmailInput(attrs={
                "class": "validate",
                "id": "email",
                "type": "text",
                "placeholder": "Enter E-mail"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "validate",
                "id": "password1",
                "type": "password",
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "validate",
                "id": "password2",
                "type": "password",
            })
        }


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "validate",
                "id": "username",
                "type": "text",
            }),
            "password": forms.PasswordInput(attrs={
                "class": "validate",
                "id": "password",
                "type": "password"
            })
        }

