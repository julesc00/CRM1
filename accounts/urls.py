from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register_page, name="register-page"),
    path('login/', views.login_page, name="login-page"),
    path('logout/', views.logout_user, name="logout"),

    path('', views.index, name="index"),
    path('user/', views.user_page, name="user-page"),

    path('customer/<str:pk>/', views.list_customer, name="customer"),
    path('create_customer', views.create_customer, name="create-customer"),
    path('update_customer/<str:pk>/', views.update_customer, name="update-customer"),
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete-customer"),

    path('products/', views.list_products, name="products"),
    path('create_order/<str:pk>/', views.create_order, name="create-order"),
    path('update_order/<str:pk>/', views.update_order, name="update-order"),
    path('delete_order/<int:pk>/', views.delete_order, name="delete-order"),
]
