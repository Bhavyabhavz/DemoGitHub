from django.db import models


# Create your models here.
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class book(models.Model):
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_price = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    book_img = models.ImageField(upload_to='book_img/')

    class Meta:
        db_table = 'bookstore'


class SIGNUP(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'signup'
