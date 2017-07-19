# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Userlikes,News
from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from mynews.forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.validators import validate_email
# Create your views here.

def login_view(request):
    errors=[]
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print request.user
            return redirect('/')
        else:
            errors.append('please input correct username & password')
    return render_to_response('mynews/login.html',RequestContext(request,{'errors':errors}))

def logout_view(request):
    logout(request)
    return redirect('/')

    
def register_view(request):
    errors=[]
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if "@" and "."not in email:#验证邮箱合法
            errors.append(u"the email  have valiad")
        elif  User.objects.all().filter(email = email):#验证是否邮箱已被注册
            errors.append(u"the email  have exist")
        elif User.objects.all().filter(username = username):#验证是否用户名已被注册
            errors.append(u"the username have exist")
        elif  len(password) < 8 :
            errors.append(u"password atlest 8 charcholate ")
        elif password != password2:
            errors.append(u"please inpput same password")                                
        else:
            user=User.objects.create_user(username=username,email=email,password=password)#不用create_user会导致密码没有hash处理会无法登陆
            user.save()
            return render(request,'mynews/success.html',{'user':user})
    return render_to_response('mynews/register.html',RequestContext(request,{'errors':errors}))
'''

    if request.method=="POST":
        form=RegisterForm()
        if form.is_valid():            
            username = form.clean_data['username']
            email = form.clean_data['email']
            password = form.clean_data['password']
            password2 = form.clean_data['password2']
            user=User.objects.create_user(username,email,password)
            user.save() 
            return render(request,'mynews/success.html',{'user':user})
    else:
        form = RegisterForm()
    return render_to_response('mynews/register.html',RequestContext(request,{'form':form}))'''