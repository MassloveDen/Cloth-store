from django.db import models

# Create your models here.
from userss.models import User


class Catalog(models.Model):
    name = models.CharField(max_length=64, unique=True)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Каталог товаров'

    def __str__(self):
        return self.name

class Production(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='production_images', blank=True)
    details = models.TextField(blank=True)
    desc = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quant = models.PositiveIntegerField(default=0)
    categor = models.ForeignKey(Catalog, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}|{self.categor.name}'

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Production, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Basket for {self.user.username}| Product {self.product.name}'
    def sum(self):
        return self.quantity * self.product.price

