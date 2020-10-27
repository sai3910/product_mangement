from django.shortcuts import render
from rest_framework import filters
from rest_framework import filters, generics, mixins, permissions, status, viewsets
# Create your views here.

from .serializers import ProductSerializer, KeywordSerializer
from .models import Product, Keyword



class ProductView(mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):

    search_fields = ['brand_name','name','keywords__name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {
            "request": self.request,
            "args": self.args,
            "kwargs": self.kwargs
        }

    def get_queryset(self):

        queryset =  Product.objects.all()
        return queryset