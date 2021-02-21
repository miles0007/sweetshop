from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Commodity(models.Model):
    SALES_CHOICES = (
        ('KG', 'kg'),
        ('MG', 'mg'),
        ('PIECES', 'pieces')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    in_stock_unit = models.CharField(choices=SALES_CHOICES, max_length=10)
    in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    minimum_unit = models.CharField(max_length=20)
    is_available = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True)

    def __str__(self):
        return self.name