from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import ShortenerFactory


class ShortenerTests(APITestCase):
    def test_create_short_url(self):
        url = reverse('shortener-list')
        data = {'long_url': 'https://docs.djangoproject.com/en/4.0/topics/testing/overview/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('long_url'), data.get('long_url'))
        self.assertIsNotNone(response.data.get('slug'))
        self.assertEqual(len(response.data.get('slug')), 7)

    def test_update_short_url(self):
        instance = ShortenerFactory.create()
        url = reverse('shortener-detail', args=[instance.pk])
        data = {'long_url': 'https://docs.djangoproject.com/en/4.0/topics/testing/overview/'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('long_url'), data.get('long_url'))
        self.assertEqual(response.data.get('slug'), instance.slug)
        self.assertEqual(len(response.data.get('slug')), 7)

    def test_get_long_url(self):
        instance = ShortenerFactory.create()
        url = reverse('long_url', args=[instance.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, {'url': instance.long_url})
