from rest_framework import serializers

from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "title","publisher","publisher_name","one_price","amount",
            "amount_info","d_day","description","end_date",
            )

class ProductDetailSerializer(ProductsSerializer):
    class Meta:
        model = Product
        fields = ProductsSerializer.Meta.fields
        read_only_fields = ("amount",)