import time

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from .models import Order, Customer, Product
from .forms import OrderForm, CustomerForm


def index(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    out_for_delivery = orders.filter(status="Out for delivery").count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {
        "title": "CRM1",
        "orders": orders,
        "customers": customers,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "out_for_delivery": out_for_delivery,
        "delivered": delivered,
        "pending": pending,
    }
    return render(request, "accounts/main.html", context)


def list_products(request):
    products = Product.objects.all()
    context = {
        "title": "Products Section",
        "products": products
    }
    return render(request, "accounts/products.html", context)


def list_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {
        "title": "Customers Section",
        "customer": customer,
        "orders": orders,
        "total_orders": total_orders
    }
    return render(request, "accounts/customer.html", context)


def create_customer(request):
    """Create a new customer."""
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

            time.sleep(2)
            return redirect("accounts:index")
    else:
        form = CustomerForm()
    context = {
        "form": form
    }

    return render(request, "accounts/customer_form.html", context)


def update_customer(request, pk):
    """Update a specific customer."""
    customer = Customer.objects.get(pk=pk)
    form = CustomerForm(instance=customer)

    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()

            return redirect("accounts:index")
    context = {
        "form": form,
        "customer": customer
    }

    return render(request, "accounts/customer_form.html", context)


def delete_customer(request, pk):
    """Delete a specific customer."""
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        customer.delete()

        return redirect("accounts:index")

    context = {"customer": customer}

    return render(request, "accounts/delete_customer.html", context)


def create_order(request, pk):
    """Create a new order."""
    order_form_set = inlineformset_factory(Customer, Order, fields=("product", "status"), extra=3)
    customer = Customer.objects.get(pk=pk)
    formset = order_form_set(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={"customer": customer})

    if request.method == "POST":
        formset = order_form_set(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()

            time.sleep(2)
            return redirect("accounts:index")

    context = {"formset": formset, "customer": customer}
    return render(request, "accounts/order_form.html", context)


def update_order(request, pk):
    """Update an order."""
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

            return redirect("account:index")
    context = {
        "form": form,
        "order": order
    }

    return render(request, "accounts/order_form.html", context)


def delete_order(request, pk):
    """Delete a specific order."""
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        order.delete()

        return redirect("account:index")

    context = {
        "order": order
    }

    return render(request, "accounts/delete.html", context)
