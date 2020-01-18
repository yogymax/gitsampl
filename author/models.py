from django.db import models
from django.core.exceptions import ValidationError
import re

def checkforpunepin(pin):
    errormsg = ''
    if len(pin)!=6:
        #raise ValidationError('{} Invalid pincode--shud have 6 digits'.format(pin))
        errormsg +='{} Invalid pincode--shud have 6 digits, '.format(pin)
    if int(str(pin)[:3:])!=411:
        #raise ValidationError('{} Invalid pincode for Pune Address--shud start with 411'.format(pin))
        errormsg +='{} Invalid pincode for Pune Address--shud start with 411, '.format(pin)

    if len(errormsg)>0:
        raise ValidationError('{}'.format(errormsg))


def checkforscpemail(val):
    if 'scoopen.in' != val.split('@')[1]:
        raise ValidationError('{} Invalid Email..Allowed only SCP emails'.format(val))


def check_valid_qty(val):
    if val<=0:
        raise ValidationError('{} Invalid Qty..shud be >0'.format(val))
    elif val>1000:
        raise ValidationError('{} Invalid Qty..LIMIT EXCEED'.format(val))

# Create your models here.
class Book(models.Model):
    name = models.CharField('book_nm',max_length=100)
    price = models.FloatField('book_pr')
    qty = models.IntegerField('book_qty',validators=[check_valid_qty])
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'BOOK_INFO'
#Book(id=1222,name='AABC',price=2383,qty=-10)
class Author(models.Model):
    name = models.CharField('book_nm',max_length=100)
    expr = models.IntegerField('author_exp')
    age = models.IntegerField('author_age')
    email = models.EmailField('author_email',validators=[checkforscpemail])
    books = models.ManyToManyField(Book)
#a1 = Author(id=101,name='AAA',expr=3,age=22,email='abc@gmail.com')

class Publication(models.Model):
    name = models.CharField('pub_name',max_length=100)
    author = models.OneToOneField(Author, on_delete=models.CASCADE,null=True)

class Address(models.Model):
    city = models.CharField('city', max_length=100)
    state = models.CharField('state', max_length=100)
    pincode = models.IntegerField('pincode',validators=[checkforpunepin])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)



