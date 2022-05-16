from django.db import models


class Shortener(models.Model):
    long_url = models.URLField()
    slug = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
