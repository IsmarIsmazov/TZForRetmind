from django.http import JsonResponse
from django.core.cache import cache
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import redis
import pandas as pd
from TZForRetmind.settings import base
from .serializers import CategorySerializer, ProductSerializer, TagSerializer
from .models import Product, Tag, Category
from .permissions import IsRegisteredUserReadOnly

redis_instance = redis.StrictRedis(host=base.REDIS_HOST,
                                   port=base.REDIS_PORT, db=0)


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

    # permission_classes = [IsRegisteredUserReadOnly]

    def get(self, request, *args, **kwargs):
        cache_queryset_name = Product.objects.all()
        cache_queryset = cache.get(cache_queryset_name)
        if cache_queryset:
            total_quryset = cache_queryset
        else:
            total_quryset = Product.objects.all()
            cache.set(cache_queryset_name, total_quryset, 30)

        response_data = total_quryset
        response.data = response_data

        return response


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    # permission_classes = [IsRegisteredUserReadOnly]
    def get(self, request, *args, **kwargs):
        cache_queryset_name = Tag.objects.all()
        cache_queryset = cache.get(cache_queryset_name)
        if cache_queryset:
            total_quryset = cache_queryset
        else:
            total_quryset = Tag.objects.all()
            cache.set(cache_queryset_name, total_quryset, 30)

        response_data = total_quryset
        response.data = response_data

        return response


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # permission_classes = [IsRegisteredUserReadOnly]
    def get(self, request, *args, **kwargs):
        cache_queryset_name = Category.objects.all()
        cache_queryset = cache.get(cache_queryset_name)
        if cache_queryset:
            total_quryset = cache_queryset
        else:
            total_quryset = Category.objects.all()
            cache.set(cache_queryset_name, total_quryset, 30)

        response_data = total_quryset
        response.data = response_data

        return response
