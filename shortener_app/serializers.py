from rest_framework import serializers

from .commons import create_random_code
from .models import Shortener


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = '__all__'

    def to_internal_value(self, data):
        if self.context.get('request').method == 'POST':
            data['slug'] = create_random_code()
        return data
