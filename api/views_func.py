'''
This is the function based view for the API
'''


'''
from rest_framework.decorators import api_view
from .models import Product, Order
from rest_framework.response import Response
from .serializers import ProductInfoSerializer, ProductSerializer, OrderSerializer
from django.db.models import Max


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
    orders = Order.objects.prefetch_related('items__product')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET']) 
def product_info(request):
     products = Product.objects.all()
     serializer = ProductInfoSerializer({
         'products': products,
         'count': products.count(),
         'max_price': products.aggregate(max_price=Max('price'))['max_price']
     })
     return Response(serializer.data)

'''