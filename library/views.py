from django.shortcuts import render
from . import serializers
from . import models
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView
from django.http import Http404



# Create your views here.
class CategoryCreate(CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    

class CategoryView(RetrieveAPIView):
    queryset = models.Category.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.CategorySerializer

class CategoryList(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_fields = ('name','id')

class CategoryUpdate(RetrieveUpdateAPIView):
    queryset = models.Category.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.CategorySerializer

class CategoryDestroy(DestroyAPIView):
    queryset = models.Category.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.CategorySerializer


class BookCreate(CreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

class BookList(ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

class BookView(RetrieveAPIView):
    queryset = models.Book.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.BookSerializer

class BookUpdate(RetrieveUpdateAPIView):
    queryset = models.Book.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.BookSerializer

class BookDestroy(DestroyAPIView):
    queryset = models.Book.objects.all()
    lookup_field = 'pk'
    serializer_class = serializers.BookSerializer

class BookCategoryList(ListAPIView):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        try:
            category = models.Category.objects.get(id=self.kwargs['category_id'])
        except models.Category.DoesNotExist:
            raise Http404("Category does not exist")

        return models.Book.objects.filter(category=category)