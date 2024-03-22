# order/factories.py

import factory
from django.contrib.auth.models import User  

from order.models import Order  

class UserFactory(factory.django.DjangoModelFactory):  # Modifique DjangoModeFactory para DjangoModelFactory
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
    
    class Meta:
        model = User

class ProductFactory(factory.django.DjangoModelFactory):  # Modifique DjangoModeFactory para DjangoModelFactory
    user = factory.SubFactory(UserFactory)
    
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.category.add(category)

    class Meta:
        model = Order
        skip_postgeneration_save = True 
