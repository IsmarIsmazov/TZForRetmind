from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)
router.register('tag', TagViewSet)


urlpatterns = router.urls
