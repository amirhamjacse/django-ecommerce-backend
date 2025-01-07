from django.shortcuts import render
from products.models import Product
from rest_framework.views import APIView
from products.serializer import (
    ProductSerializer, ProductAddSerializer
)
from rest_framework.response import Response
from rest_framework import status


class ProductView(APIView):
    def get(self, request):
        product_obj = Product.objects.all()
        serializer = ProductSerializer(product_obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        # product_obj = Product.objects.all()
        serializer = ProductAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        pass

    def put(self, request):
        pass
    
    def delete(self, request):
        pass





