from rest_framework.serializers import ModelSerializer
from apps.article.models import Book, Category, Comment


class CommentSerializer(ModelSerializer):

    def save(self, **kwargs):
        super(CommentSerializer, self).save(**kwargs)

    class Meta:
        model = Comment
        fields = "__all__"