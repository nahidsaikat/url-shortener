from django.urls import path
from rest_framework import routers

from .views import ShortenerViewSet, LongURLViewSet

router = routers.SimpleRouter()
router.register(r'shortener', ShortenerViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('<slug:str>/', LongURLViewSet.as_view({'get': 'retrieve'})),
]
