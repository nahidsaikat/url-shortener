from string import ascii_letters, digits
from random import choice

from django.conf import settings


SIZE = settings.MAX_URL_CHARS
AVAILABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAILABLE_CHARS):
    return "".join([choice(chars) for _ in range(SIZE)])
