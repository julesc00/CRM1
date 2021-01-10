import time

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Order, Customer, Product
from .forms import OrderForm, CustomerForm, CreateUserForm
from .filters import OrderFilter


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account was created for {username}")

            return redirect("accounts:login-page")

    context = {"form": form}

    return render(request, "accounts/register.html", context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("accounts:index")
    else:
        if request.method == "POST":
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                if next in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect("accounts:index")
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)


def logout_user(request):
    logout(request)
    return redirect("accounts:login-page")


@login_required(login_url="accounts:login-page")
def index(request):
    orders = Order.objects.all()
    orders_list = Order.objects.all()
    customers = Customer.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(orders_list, 5)

    try:
        orders2 = paginator.page(page)
    except PageNotAnInteger:
        orders2 = paginator.page(1)
    except EmptyPage:
        orders2 = paginator.page(paginator.num_pages)

    total_customers = customers.count()
    total_orders = orders.count()
    out_for_delivery = orders.filter(status="Out for delivery").count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {
        "title": "CRM1",
        "orders": orders,
        "orders2": orders2,
        "customers": customers,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "out_for_delivery": out_for_delivery,
        "delivered": delivered,
        "pending": pending,

    }
    return render(request, "accounts/main.html", context)


@login_required(login_url="accounts:login-page")
def list_products(request):
    products = Product.objects.all()
    context = {
        "title": "Products Section",
        "products": products
    }
    return render(request, "accounts/products.html", context)


@login_required(login_url="accounts:login-page")
def list_customer(request, pk):
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    total_orders = orders.count()

    customer_filter = OrderFilter(request.GET, queryset=orders)
    orders = customer_filter.qs

    context = {
        "title": "Customers Section",
        "customer": customer,
        "orders": orders,
        "total_orders": total_orders,
        "customer_filter": customer_filter
    }
    return render(request, "accounts/customer.html", context)


@login_required(login_url="accounts:login-page")
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


@login_required(login_url="accounts:login-page")
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


@login_required(login_url="accounts:login-page")
def delete_customer(request, pk):
    """Delete a specific customer."""
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        customer.delete()

        return redirect("accounts:index")

    context = {"customer": customer}

    return render(request, "accounts/delete_customer.html", context)


@login_required(login_url="accounts:login-page")
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


@login_required(login_url="accounts:login-page")
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


@login_required(login_url="accounts:login-page")
def delete_order(request, pk):
    """Delete a specific order."""
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        order.delete()

        return redirect("accounts:index")

    context = {
        "order": order
    }

    return render(request, "accounts/delete.html", context)
