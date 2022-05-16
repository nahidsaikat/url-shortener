from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .models import Shortener
from .serializers import ShortenerSerializer


class ShortenerViewSet(viewsets.ModelViewSet):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerSerializer


class LongURLViewSet(mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    def retrieve(self, request, *args, **kwargs):
        instance = Shortener.objects.get(slug=kwargs.get('slug'))
        return Response({'url': instance.long_url})
