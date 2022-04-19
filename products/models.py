from datetime import datetime

from django.db import models

from accounts.models import Account


class Product(models.Model):
    title       = models.CharField(max_length=200, unique=True)
    publisher   = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount      = models.IntegerField()
    end_date    = models.DateTimeField()
    one_price   = models.IntegerField()
    fund        = models.ManyToManyField(Account, related_name='fund', through='Pd_fund')
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.title

    def publisher_name(self):
        return self.publisher.username

    def amount_info(self):
        person_count = self.pd_fund_set.count()
        amount_price = person_count * self.one_price
        return {"price": amount_price, "percent": round(amount_price*100/self.amount), "person_count": person_count}

    def d_day(self):
        date = (self.end_date-datetime.now()).days
        if date < 0:
            return "종료"
        return date

class Pd_Fund(models.Model):
    account    = models.ForeignKey(Account, on_delete=models.PROTECT)
    product    = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)