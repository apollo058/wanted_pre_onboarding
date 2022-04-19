from rest_framework import serializers

from .models import Pd_Fund, Product


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id","title","publisher","publisher_name","one_price","amount",
            "amount_info","d_day","description","end_date",
            )

class ProductDetailSerializer(ProductsSerializer):
    class Meta:
        model = Product
        fields = ProductsSerializer.Meta.fields
        read_only_fields = ("amount",)

class Pd_FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pd_Fund
        fields = ("id", "account", "product", "created_at", "updated_at")