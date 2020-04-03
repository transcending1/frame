from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.article.models import Book, Chapter, Category
from apps.article.serializers.book import BookSerializer, BookCommentSerializer
from apps.article.serializers.category import CategorySerializer
from apps.article.serializers.chapter import ChapterSerializer
from utils.pagination import StandardPageNumberPagination


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
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
        return super(CategoriesViewSet, self).list(request, *args, **kwargs)

    # @cache_response()
    def list(self, request, *args, **kwargs):
        return super(CategoriesViewSet, self).list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     super(CategoriesViewSet, self).create()
