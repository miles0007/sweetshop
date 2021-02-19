from django.db import models

# Create your models here.

class Commodity(models.Model):
    SALES_CHOICES = (
        ('KG', 'kg'),
        ('MG', 'mg'),
        ('PIECES', 'pieces')
    )
    name = models.CharField(max_length=100)
    in_stock_unit = models.CharField(choices=SALES_CHOICES, max_length=10)
    in_stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField(help_text="For 100 Mg of Product")
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.name