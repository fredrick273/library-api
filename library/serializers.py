from .models import Category,Book,Person,LendingHistory
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

    def validate_name(self,value):
        exsisting = Category.objects.filter(name=value).exclude(id=self.instance.id if self.instance else None).first()
        if exsisting:
            raise serializers.ValidationError("A category with this name already exists.")
        return value
    
class BookSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only = True, allow_null=True)
    category_name = serializers.StringRelatedField(source='category',read_only=True)
    class Meta:
        model = Book
        fields = ["id", "title",'author','language','publisher','category','category_name']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name','age']


class LenderHistorySerializer(serializers.ModelSerializer):
    person = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all())
    person_name = serializers.StringRelatedField(source='person',read_only=True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_name = serializers.StringRelatedField(source='book',read_only=True)

    class Meta:
        model = LendingHistory
        fields = ['id', 'person','person_name','book','book_name','borrowing_time','returning_time' ]
        
