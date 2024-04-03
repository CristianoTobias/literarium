from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
import json
from product.factories import CategoryFactory
from product.models import Category

class TestCategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='books')

    def test_get_all_category(self):
        response = self.client.get(reverse('category-list', kwargs={'version': 'v1'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)
        self.assertEqual(category_data['results'][0]['title'], self.category.title)

    def test_create_category(self):
        data = json.dumps({
            'title': 'technology'
        })
        response = self.client.post(reverse('category-list', kwargs={'version': 'v1'}), data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_category = Category.objects.get(title='technology')
        
        self.assertEqual(created_category.title, 'technology')
    def test_update_category(self):
        new_title = 'updated category'
        
        # Realiza uma requisição PUT para atualizar a categoria
        response = self.client.put(
            reverse('category-detail', kwargs={'version': 'v1', 'pk': self.category.id}), 
            data=json.dumps({'title': new_title}),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifica se a categoria foi atualizada corretamente no banco de dados
        updated_category = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_category.title, new_title)
