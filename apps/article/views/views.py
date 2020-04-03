from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.article.models import Book, Chapter, Category, Comment
from apps.article.serializers.book import BookSerializer, BookCommentSerializer
from apps.article.serializers.category import CategorySerializer
from apps.article.serializers.chapter import ChapterSerializer
from apps.article.serializers.comment import CommentSerializer
from utils.pagination import StandardPageNumberPagination


class BooksViewSet(ModelViewSet):
    """小说相关视图集,提供小说列表,小说详情和评论,小说详情修改等"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        """重写retrieve方法,当获取单本小说详情时,返回评论内容"""
        instance = self.get_object()
        serializer = BookCommentSerializer(instance)

        return Response(serializer.data)


class ChaptersViewSet(ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class CategoriesViewSet(ModelViewSet):
    queryset = Category.objects.filter(sub=None)
    serializer_class = CategorySerializer
    pagination_class = StandardPageNumberPagination

    def get_queryset(self, **kwargs):
        if self.action == "category":
            return Category.objects.filter(id=self.kwargs['pk']).first().book.all()
        return self.queryset

    def get_serializer_class(self):
        if self.action == "category":
            return BookSerializer

        return self.serializer_class

    @action(methods=['get'], detail=True)
    def category(self, request, *args, **kwargs):
        """对获取分类书籍添加方法,该方法返回该分类下的所有书籍,并提供分页"""
        return super(CategoriesViewSet, self).list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):

        return super(CategoriesViewSet, self).list(request, *args, **kwargs)


class CommentsViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


