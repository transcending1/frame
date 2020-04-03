from rest_framework.serializers import ModelSerializer
from apps.article.models import Book, Category


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CategoryBookSerializer(ModelSerializer):
    book = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = "__all__"
