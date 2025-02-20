from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerailzer, ProductInfoSerializer
from rest_framework.response import Response
from django.db.models import Max
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# @api_view(['GET'])
# def product_lists(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

# @api_view(['GET'])
# def product_list(request, pk):
#     product = Product.objects.get(pk=pk)
#     serializer = ProductSerializer(product)
#     return Response(serializer.data)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

# @api_view(['GET'])
# def order_lists(request):
#     orders = Order.objects.prefetch_related('items__product')
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer

    
class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

@api_view(['GET']) 
def product_info(request):
     products = Product.objects.all()
     serializer = ProductInfoSerializer({
         'products': products,
         'count': products.count(),
         'max_price': products.aggregate(max_price=Max('price'))['max_price']
     })
     return Response(serializer.data)
