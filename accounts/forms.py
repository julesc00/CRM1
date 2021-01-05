from django import forms

from .models import Order, Customer, Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer", "product", "status"]

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
            "status": forms.TextInput(attrs={
                "class": "validate",
                "id": "status",
                "type": "text"
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
