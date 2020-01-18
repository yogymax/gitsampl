from django.db import models


class BookInfo(models.Model):
    #bookid = models.IntegerField(primary_key=True)
    name = models.CharField('book_name',max_length=100)
    price = models.FloatField('book_price')
    category=models.CharField('book_cate',max_length=100)
    publication=models.CharField('book_publ',max_length=100)
    quantity = models.IntegerField('book_qty')
    #authors


class Author(models.Model):
    name = models.CharField('author_name', max_length=100)
    city = models.CharField('author_address', max_length=100)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,related_name='authors')



