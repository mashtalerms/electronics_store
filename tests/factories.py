import factory

from core.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    first_name = 'Test name'
    last_name = 'Test name'
    email = 'email@mail.ru'
    password = 'fdsfds2542g'
