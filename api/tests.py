from django.test import TestCase
from .models import User, Order
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class UserOrderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='test@123')
        user2 = User.objects.create_user(username='user2', password='test@123')
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user2)
    
    def test_user_order(self):
        user = User.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-orders'))
        
        assert response.status_code == status.HTTP_200_OK
        
        orders = response.json()
        self.assertTrue(all(order['user'] == user.username for order in orders))
        
    def test_user_unauthenticate(self):
        response = self.client.get(reverse('user-orders'))
        self.assertTrue(response.status_code, status.HTTP_403_FORBIDDEN)