from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    language = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
    
class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class LendingHistory(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrowing_time = models.DateField(auto_now_add=True)
    returning_time = models.DateField(null=True)

    def __str__(self):
        return str(self.person) + ' - ' + str(self.book)