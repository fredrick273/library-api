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
    
class PersonBorrowedList(ListAPIView):
    serializer_class = serializers.LenderHistorySerializer

    def get_queryset(self):
        try:
            person = models.Person.objects.get(id=self.kwargs['person_id'])
        except models.Person.DoesNotExist:
            raise Http404("Person does not exist")

        return models.LendingHistory.objects.filter(person=person,returning_time__isnull=True)
    
class PersonReturnedList(ListAPIView):
    serializer_class = serializers.LenderHistorySerializer

    def get_queryset(self):
        try:
            person = models.Person.objects.get(id=self.kwargs['person_id'])
        except models.Person.DoesNotExist:
            raise Http404("Person does not exist")

        return models.LendingHistory.objects.filter(person=person,returning_time__isnull=False)
    
class BorrowedList(ListAPIView):
    serializer_class = serializers.LenderHistorySerializer
    queryset = models.LendingHistory.objects.filter(returning_time__isnull=True)

class ReturnedList(ListAPIView):
    serializer_class = serializers.LenderHistorySerializer
    queryset = models.LendingHistory.objects.filter(returning_time__isnull=False)
    
class PersonList(ListAPIView):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()

class PersonCreate(CreateAPIView):
    serializer_class = serializers.PersonSerializer
    queryset = models.Person.objects.all()

class PersonView(RetrieveAPIView):
    serializer_class = serializers.PersonSerializer
    lookup_field = 'pk'
    queryset = models.Person.objects.all()

class PersonUpdate(RetrieveUpdateAPIView):
    serializer_class = serializers.PersonSerializer
    lookup_field = 'pk'
    queryset = models.Person.objects.all()

class PersonDestroy(DestroyAPIView):
    serializer_class = serializers.PersonSerializer
    lookup_field = 'pk'
    queryset = models.Person.objects.all()

class LendingHistoryList(ListAPIView):
    serializer_class = serializers.LenderHistorySerializer
    queryset = models.LendingHistory.objects.all()

class LendingHistoryCreate(CreateAPIView):
    serializer_class = serializers.LenderHistorySerializer
    queryset = models.LendingHistory.objects.all()

class LendingHistoryView(RetrieveAPIView):
    serializer_class = serializers.LenderHistorySerializer
    lookup_field = 'pk'
    queryset = models.LendingHistory.objects.all()

class LendingHistoryUpdate(RetrieveUpdateAPIView):
    serializer_class = serializers.LenderHistorySerializer
    lookup_field = 'pk'
    queryset = models.LendingHistory.objects.all()

class LendingHistoryDestroy(DestroyAPIView):
    serializer_class = serializers.LenderHistorySerializer
    lookup_field = 'pk'
    queryset = models.LendingHistory.objects.all()
