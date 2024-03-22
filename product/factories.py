import factory

from product.models import Order

class UserFactory(factory.django.DjangoModeFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
    
    class Meta:
        model = User

class ProductFactory(factory.django.DjangoModeFactory):
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