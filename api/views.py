from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer, ProductInfoSerializer
from rest_framework.response import Response
from django.db.models import Max
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter, IsStockFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets


# Create your views here.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, IsStockFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'stock']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 2
    pagination_class.page_size_query_param = 'size' #Max data that the api can return
    pagination_class.max_page_size=4
    pagination_class.page_query_param = 'p'

    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class ProductDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items__product').order_by('pk')
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    
# class OrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.prefetch_related('items__product')
#     serializer_class = OrderSerializer


# class UserOrderListAPIView(generics.ListAPIView):
#     queryset = Order.objects.prefetch_related('items__product')
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(user=self.request.user)


class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': products.count(),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)

