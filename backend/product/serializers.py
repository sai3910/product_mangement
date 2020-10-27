from rest_framework import serializers
from .models import Product, Keyword


class ProductSerializer(serializers.ModelSerializer):
    keywords = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ('id', 'brand_name','name', 'offer_price', 'mrp','image_url','keywords')



class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ('id', 'name', )
