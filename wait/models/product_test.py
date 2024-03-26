from django.test import TestCase
from product.models import Product, Category

class ProductModelTestCase(TestCase):
    def setUp(self):
        # Crie uma categoria de exemplo
        self.category = Category.objects.create(title='Electronics')

        # Crie um produto de exemplo
        self.product = Product.objects.create(
            title='Smartphone',
            description='A great smartphone',
            price=500,
            active=True
        )
        self.product.category.add(self.category)

    def test_product_creation(self):
        # Verifique se o produto foi criado corretamente
        self.assertEqual(self.product.title, 'Smartphone')
        self.assertEqual(self.product.description, 'A great smartphone')
        self.assertEqual(self.product.price, 500)
        self.assertTrue(self.product.active)
        self.assertEqual(self.product.category.count(), 1)
        self.assertEqual(self.product.category.first(), self.category)