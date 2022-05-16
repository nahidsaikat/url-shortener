import boto3

from django.conf import settings
from rest_framework import viewsets
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
    client = boto3.client('dynamodb', profile=settings.AWS_PROFILE)
    client.put_item(TableName=settings.AWS_DYNAMODB_TABLE_NAME, Item={
        'long_url': {'S': instance.long_url}, 'slug': {'S': instance.slug}})
    return Response({'url': instance.long_url})


@api_view(['GET'])
def get_count(request, slug):
    instance = Shortener.objects.get(slug=slug)
    client = boto3.client('dynamodb', profile=settings.AWS_PROFILE)
    response = client.query(
        TableName=settings.AWS_DYNAMODB_TABLE_NAME,
        KeyConditionExpression='slug = :slug',
        ExpressionAttributeValues={
            ':slug': {'S': instance.slug}
        }
    )
    return Response({'count': response.get('Count')})
