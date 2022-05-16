from django.urls import path
from rest_framework import routers

from .views import ShortenerViewSet, long_url, get_count

router = routers.SimpleRouter()
router.register(r'shortener', ShortenerViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('<slug:slug>/', long_url, name='long_url'),
    path('<slug:slug>/count/', get_count, name='get_count'),
]
