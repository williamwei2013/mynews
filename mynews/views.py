# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from news.models import Userlikes,News
from django.shortcuts import render,render_to_response,get_object_or_404
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from mynews.forms import LoginForm,UserForm
from news.forms import UserprofileForm
from django.contrib.auth import authenticate, login,logout
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.core.validators import validate_email
import json
from django.http import JsonResponse
from django.http import HttpResponse
from news.serializers import  *
from rest_framework import viewsets


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
    return render(request,'mynews/login.html',{'errors':errors})

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
            errors.append(u"邮箱格式不正确")
        elif  User.objects.all().filter(email = email):#验证是否邮箱已被注册
            errors.append(u"您输入的邮箱已存在")
        elif User.objects.all().filter(username = username):#验证是否用户名已被注册
            errors.append(u"您输入的用户名已存在")
        elif  len(password) < 8 :
            errors.append(u"密码不能少于8个字符 ")
        elif password != password2:
            errors.append(u"两次输入密码不一致")                                
        else:
            user=User.objects.create_user(username=username,email=email,password=password)#不用create_user会导致密码没有hash处理会无法登陆
            user.save()
            return render(request,'mynews/success.html',{'user':user})
    return render(request,'mynews/register.html',{'errors':errors})

def register_check(request):
    if request.method=="POST":
        email=request.POST['email']
        if User.objects.all().filter(email = email):
            return HttpResponse('-1')
        else:
            return HttpResponse('1')
    else:
        return HttpResponse('0')



def register_demo(request):
    return render(request,'mynews/register_demo.html')  
    
class NewsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer   

  
class UserViewSet(viewsets.ModelViewSet):  
    """ 
    API endpoint that allows users to be viewed or edited. 
    """  
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    
'''
def register_view(request):
    registered = False
    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserprofileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserprofileForm()
    return render(request,'mynews/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})'''