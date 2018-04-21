from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=40, unique=True)

class Burger(models.Model):
    name = models.CharField(max_length=40, unique=True)
    has_bun = models.BooleanField()
    has_patty = models.BooleanField()
    toppings = models.ManyToManyField(Topping)
