from rest_framework.serializers import ModelSerializer

from apps.article.models import Category
from apps.article.serializers.book import BookSerializer


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    category = SubCategorySerializer(many=True, required=False)
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
