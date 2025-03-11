from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    net_worth = models.DecimalField(decimal_places=2, max_digits=100)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField()
    markets = models.ManyToManyField(Market, related_name='sellers')

    # def __str__(self):
    #     return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=50)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='products')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name} ({self.price})"
