from django.shortcuts import render
from products.models import Product
from rest_framework.views import APIView
from products.serializer import ProductSerializer
from rest_framework.response import Response


class ProductView(APIView):
    def get(self, request):
        product_obj = Product.objects.all()
        serializer = ProductSerializer(product_obj, many=True)
        return Response(serializer.data)
