from rest_framework import serializers

from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("title","publisher_name","one_price","amount_info","d_day","description")
        read_only_fields = ("amount", "amount_price")