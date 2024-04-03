from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
import json
from product.factories import ProductFactory, CategoryFactory
from order.factories import UserFactory
from product.models import Product

class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.product = ProductFactory(title='pro controller', price=200.00)
        
 
    def test_get_all_product(self):
        response = self.client.get(reverse('product-list', kwargs={'version': 'v1'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)
        self.assertEqual(product_data['results'][0]['title'], self.product.title)
        self.assertEqual(product_data['results'][0]['price'], self.product.price)
        self.assertEqual(product_data['results'][0]['active'], self.product.active)
        

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps({
            'title': 'notebook',
            'price': 800.00,
            'categories_id': [category.id]
        })
        response = self.client.post(reverse('product-list', kwargs={'version': 'v1'}), data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_product = Product.objects.get(title='notebook')
        
        self.assertEqual(created_product.title, 'notebook')
        self.assertEqual(created_product.price, 800.00)

    def test_update_product(self):
        new_title = 'updated product'
        new_price = 300.00
        category = CategoryFactory()  # Cria uma nova categoria para o produto atualizado
        
        # Realiza uma requisição PUT para atualizar o produto
        response = self.client.put(
            reverse('product-detail', kwargs={'version': 'v1', 'pk': self.product.id}), 
            data=json.dumps({
                'title': new_title,
                'price': new_price,
                'categories_id': [category.id]  # Fornecendo o campo categories_id
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifica se o produto foi atualizado corretamente no banco de dados
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.title, new_title)
        self.assertEqual(updated_product.price, new_price)

    def test_update_product_2(self):
        new_title = 'Iphone'
            
        # Realiza uma requisição PATCH para atualizar apenas o título do produto
        response = self.client.patch(
                reverse('product-detail', kwargs={'version': 'v1', 'pk': self.product.id}), 
                data=json.dumps({
                    'title': new_title,
                }),
                content_type='application/json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            
        # Verifica se o produto foi atualizado corretamente no banco de dados
        updated_product = Product.objects.get(id=self.product.id)
        self.assertEqual(updated_product.title, new_title)
    def test_delete_product(self):
        # Realiza uma requisição DELETE para deletar o produto
        response = self.client.delete(reverse('product-detail', kwargs={'version': 'v1', 'pk': self.product.id}))
    
        # Verifica se o produto foi deletado corretamente
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
        # Verifica se o produto não está mais presente no banco de dados
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=self.product.id)