from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'slug',
            'description',
            'category',
            'tags',
            'price',
            'discount_price',
            'stock',
            'is_active',
            'image',
            'additional_images',
            'created_at',
            'updated_at',
        ]
