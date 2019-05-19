from datetime import date
from django import forms

from django.db import models
        
# Create your models here.
class Book(models.Model):#книга
    number_code=models.CharField(max_length=10)#код книги
    title=models.CharField(max_length=100)#название/загаловок
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)#ссылка на автора книги
    pic=models.CharField(max_length=250, default='', null=True, blank=True)#ссылка на картинку
    description=models.CharField(max_length=5000, default='', null=True, blank=True)#описание книги
    def __str__(self):
        return self.title



class Author(models.Model):#автор книги
    first_name = models.CharField(max_length=100)#имя
    last_name = models.CharField(max_length=100)#фамилия
    middle_name = models.CharField(max_length=100, default=' ', null=True, blank=True)#отчество
    pic=models.CharField(max_length=250, default=' ', null=True, blank=True)#ссылка на картинку
    description=models.CharField(max_length=5000, default='', null=True, blank=True)#описание автора
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
        
class A_Logger(models.Model):#запись о выдаче книги
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)#ссылка на книгу
    borrower = models.ForeignKey('Log_user' , on_delete=models.SET_NULL, null=True, blank=True)#ссылка на пользователя
    
    LOAN_STATUS = (
        ('On loan', 'On loan'),#не в наличии
        ('Available', 'Available'),#имеется в наличии
        ('Reserved', 'Reserved'),#зарезервирована
    )#типы записи

    status = models.CharField(
        max_length=10,
        choices=LOAN_STATUS,
        blank=True,
        default='Available',
        help_text='Book availability')#статус записи
    
    start_date = models.DateField(blank=True, null=True)#дата взятия книги
    finish_date = models.DateField(blank=True, null=True)#дата сдачи книги
    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1}): {2}'.format(self.borrower, self.book, self.status)       
		
class Log_user(models.Model):#пользователь
    number_code=models.CharField(max_length=10)#код читательского билета
    first_name=models.CharField(max_length=100)#имя
    last_name=models.CharField(max_length=100)#фамилия
    middle_name = models.CharField(max_length=100, default='', null=True, blank=True)#отчество
    number_phone=models.CharField(max_length=15, default='')#телефон
    pic=models.CharField(max_length=250, default='', null=True, blank=True)#ссылка на картинку
    description=models.CharField(max_length=5000, default='', null=True, blank=True)#описание пользователя
    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1}'.format(self.first_name, self.last_name) 


