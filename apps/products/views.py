from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
import pandas as pd
from .serializers import CategorySerializer, ProductSerializer, TagSerializer
from .models import Product, Tag, Category
from .permissions import IsRegisteredUserReadOnly


class Export(APIView):
    def get(self, request):
        objs = Product.objects.all()
        data = []

        for obj in objs:
            data.append({
                'name': obj.name,
                'category': obj.category,
                'tag': obj.tag,
                'description': obj.descriprion,
                'price': obj.price,
            })
        pd.DataFrame(data).to_excel('product.xlsx')
        return JsonResponse({
            'status': 200
        })


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
