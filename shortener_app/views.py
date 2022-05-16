from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Shortener
from .serializers import ShortenerSerializer


class ShortenerViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer

    def get_serializer_context(self):
        return {'request': self.request}


@api_view(['GET'])
def long_url(request, slug):
    instance = Shortener.objects.get(slug=slug)
    return Response({'url': instance.long_url})
