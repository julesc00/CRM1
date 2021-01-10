from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Capitalize first letter of name and lastname."""
        self.name = self.name.title()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = [
        ("Indoor", "Indoor"),
        ("Out Door", "Out Door"),
    ]
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def clean(self):
        """Title the product name."""
        self.name = self.name.title()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = [
        ("Pending", "Pending"),
        ("Out for delivery", "Out for delivery"),
        ("Delivered", "Delivered"),
    ]
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.name
