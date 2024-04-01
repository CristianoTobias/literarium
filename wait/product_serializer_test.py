from django.test import TestCase
from product.models import Product, Category
from product.serializers import ProductSerializer

class ProductSerializerTestCase(TestCase):
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

    def test_product_serializer(self):
        # Serializar o produto
        serializer = ProductSerializer(instance=self.product)

        # Verificar se os dados serializados correspondem aos atributos do produto
        self.assertEqual(serializer.data['title'], 'Smartphone')
        self.assertEqual(serializer.data['description'], 'A great smartphone')
        self.assertEqual(serializer.data['price'], 500)
        self.assertTrue(serializer.data['active'])

        # Verificar se a categoria está correta
        categories_data = serializer.data['category']
        self.assertEqual(len(categories_data), 1)  # Verificar se há apenas uma categoria
        self.assertEqual(categories_data[0]['title'], 'Electronics')
