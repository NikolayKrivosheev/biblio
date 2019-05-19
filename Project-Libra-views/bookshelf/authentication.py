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

def authorization(request):#вход в учетную запись
    logout(request)#выход из учетной записи пользователя
    
    user=""
    password=""
    comment=""
    if request.POST:
        #считывание размеров таблицы
        user = request.POST.get('login', '')
        password = request.POST.get('password', '')
        button = request.POST.get('button', '')
        #user = User.objects.create_user(login, '', password)
        #user.save()
        if(button=="Регистрация"):
            try:
                user = User.objects.create_user(user, '', password)
                user.save()
                user.groups.add(Group.objects.get(name="admin"))
            except:
                comment="Пользователь существует. "
    user = authenticate(username=user, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            #print("DO: ", str(request.user.is_authenticated()))
            #print("POSLE: ", request.user.is_authenticated())
            login(request, user)
            return HttpResponseRedirect('http://127.0.0.1:8000/')
            comment=comment+"Пользователь действителен, активен и аутентифицирован"
        else:
            comment=comment+"Пароль действителен, но учетная запись была отключена!"
    else:
        comment=comment+"Имя пользователя и пароль были неверны."
   
    return render(request, 'bookshelf/authorization.html', {'login': user, 'password': password, 'comment': comment})


