# order/tests/test_factories.py

from django.test import TestCase
from order.factories import UserFactory, ProductFactory
from faker import Faker

class OrderFactoryTestCase(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsNotNone(user)

    def test_product_factory(self):
        product = ProductFactory()
        self.assertIsNotNone(product)

class OrderFactoryTestCase(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsNotNone(user)

    def test_product_factory(self):
        product = ProductFactory()
        self.assertIsNotNone(product)

    def test_order_status(self):
        order = ProductFactory.create(status='Processing')
        self.assertEqual(order.status, 'Processing')

