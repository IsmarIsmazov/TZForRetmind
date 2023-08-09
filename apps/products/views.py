from django.shortcuts import render
from .serializers import CategorySerializer, ProductSerializer, TagSerializer
from .models import Product, Tag, Category
from rest_framework.viewsets import ModelViewSet
from .permissions import IsRegisteredUserReadOnly


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsRegisteredUserReadOnly]


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsRegisteredUserReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsRegisteredUserReadOnly]
