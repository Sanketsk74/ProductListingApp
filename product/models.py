
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Product(models.Model):
    productName = models.CharField( max_length=50,validators=[MinLengthValidator(3)])
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    