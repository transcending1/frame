from rest_framework.serializers import ModelSerializer
from apps.article.models import Book, Category
from apps.article.serializers.comment import CommentSerializer

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CategoryBookSerializer(ModelSerializer):
    book = BookSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = "__all__"


class BookCommentSerializer(ModelSerializer):
    """获取书籍详情和其下评论"""
    comment = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = "__all__"
