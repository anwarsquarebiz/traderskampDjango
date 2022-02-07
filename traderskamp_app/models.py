from symtable import Symbol
from django.db import models

# Create your models here.

# Assets Models
class Assets(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    symbol = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=150, null=False)
    external_id = models.CharField(max_length=100, null=True)
    status = models.IntegerField(max_length=4, null=False)
    logo = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=8, null=False)
    change_abs = models.DecimalField(max_digits=20, decimal_places=8, null=False)
    change_pct = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    supply = models.IntegerField(max_length=20, null=False)
    volume = models.IntegerField(max_length=20, null=False)
    market_cap = models.IntegerField(max_length=20, null=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)


    
