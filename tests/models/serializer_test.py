# tests/serializers/test_order_serializer.py

from django.test import TestCase
from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product
from django.contrib.auth.models import User

class OrderSerializerTestCase(TestCase):
    def setUp(self):
        # Crie alguns produtos de exemplo para usar nos testes
        self.product1 = Product.objects.create(title='Product 1', price=10)
        self.product2 = Product.objects.create(title='Product 2', price=20)

        # Crie um usuário de exemplo
        self.user = User.objects.create(username='test_user')

        # Crie um pedido de exemplo com os produtos e o usuário
        self.order = Order.objects.create(user=self.user, status='Pending')
        self.order.product.add(self.product1, self.product2)

    def test_order_serializer(self):
        # Serializar o pedido
        serializer = OrderSerializer(instance=self.order)

        # Verificar se a soma dos preços dos produtos está correta
        total = self.product1.price + self.product2.price
        self.assertEqual(serializer.data['total'], total)
