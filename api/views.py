from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerailzer
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def product_lists(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def product_list(request, pk):
    product = Product.objects.get(pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_lists(request):
    orders = Order.objects.prefetch_related('items_product')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
    