from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name="index"),
    path('customer/<int:pk>/', views.list_customer, name="customer"),
    path('create_customer', views.create_customer, name="create-customer"),
    path('update_customer/<int:pk>/', views.update_customer, name="update-customer"),
    path('delete_customer/<int:pk>/', views.delete_customer, name="delete-customer"),
    path('products/', views.list_products, name="products"),
    path('create_order/', views.create_order, name="create-order"),
    path('update_order/<int:pk>/', views.update_order, name="update-order"),
    path('delete_order/<int:pk>/', views.delete_order, name="delete-order"),
]
