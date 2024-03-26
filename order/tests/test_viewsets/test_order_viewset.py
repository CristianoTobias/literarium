from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
import json
from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory, OrderFactory
from product.models import Product
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title= 'technology')
        self.product = ProductFactory(title='mouse', price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(reverse('order-list', kwargs={'version': 'v1'}))
        print('*****')
        print(response)
        print('*****')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order_data = json.loads(response.content)[0]
        self.assertEqual(order_data['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['product'][0]['category'][0]['title'], self.category.title)

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()
        print(product.id)
        data = json.dumps({
            'products_id': [product.id],
            'user': user.id
        })
        response = self.client.post(reverse('order-list', kwargs={'version': 'v1'}), data=data, content_type='application/json')
        print('$$$$$$')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response)
        print('*****')
        created_order = Order.objects.get(user=user)


