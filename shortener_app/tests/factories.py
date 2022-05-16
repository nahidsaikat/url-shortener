import random
import string
import factory
from factory import django
from faker import Faker
from shortener_app import models

fake = Faker()


class ShortenerFactory(django.DjangoModelFactory):
    class Meta:
        model = models.Shortener

    long_url = factory.LazyAttribute(lambda _: fake.image_url())
    slug = factory.LazyAttribute(lambda _: ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7)))
