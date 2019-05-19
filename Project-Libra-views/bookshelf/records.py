from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django import forms
from django.shortcuts import render
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.utils.safestring import SafeText

from django.contrib.auth.models import Permission, User, Group
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Book,Log_user,A_Logger,Author

from datetime import datetime

def records(request):
    comment=""
    color="black"
    if request.POST:
        Num1 = request.POST.get('Num1', None)
        Num2 = request.POST.get('Num2', None)
        tip = request.POST.get('tip', None)
        
        try:
            id1=Log_user.objects.get(number_code=Num2)
            id2=Book.objects.get(number_code=Num1)
            if(tip=="Взять"):
                try:
                    log=A_Logger.objects.get(book=id2, status='Reserved')
                    comment="Ошибка: книга '"+str(id2)+"' оформелана на читателя '"+str(log.borrower)+"'"
                    color="red"
                except:
                    log=A_Logger(book=id2, borrower=id1, status='Reserved', start_date=datetime.now())
                    log.save()
                    comment="Книга '"+str(id2)+"' оформлена на читателя '"+str(id1)+"'"
                    color="green"
            if(tip=="Сдать"):
                try:
                    log=A_Logger.objects.get(book=id2, borrower=id1, status='Reserved')
                    log.status="Available"
                    log.finish_date=datetime.now()
                    log.save()
                    comment="Книга '"+str(id2)+"' сдана читателем '"+str(id1)+"'"
                    color="green"
                except:
                    comment="Ошибка: запись не существует"
                    color="red"
        except:
            comment="Ошибка: не верный код книги или чит. билета"
            color="red"
    return render(request, 'bookshelf/records.html', {"login" : request.user, "comment" : comment, "color" : color})