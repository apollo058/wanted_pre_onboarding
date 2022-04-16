from django.db import models

from accounts.models import Account


class Product(models.Model):
    title       = models.CharField(max_length=200, unique=True)
    publisher   = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount      = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    end_date    = models.DateTimeField()
    one_price   = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    fund        = models.ManyToManyField(Account, related_name='fund', through='Pd_fund')
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.title

class Pd_Fund(models.Model):
    account    = models.ForeignKey(Account, on_delete=models.PROTECT)
    product    = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)