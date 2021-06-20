from django.db import models

# Create your models here.


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

