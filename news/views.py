# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from models import *
import urlparse
from django.contrib.auth.decorators import login_required 

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#以下是restframwork
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from news.models import News
from news.serializers import NewsSerializer


# Create your views here.
def index(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10) 
    page = request.GET.get('page')
    try:
        news_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_list = paginator.page(paginator.num_pages)
    context_dict = {'news_list': news_list}
    return render(request, 'news/index.html', context_dict)

def article_detail(request,id):
    news = get_object_or_404(News, id=id)
    context_dict = {'news': news }
    return render(request, 'news/article_detail.html', context_dict)
    
def about(request):
    return render_to_response( 'news/about.html')
    
@login_required    
def click_like(request,id):
    if request.method == 'GET':
        referrer=request.META['HTTP_REFERER']
        news = get_object_or_404(News, id=id)
        user=request.user
        count=Userlikes.objects.filter(news=news).filter(user=user).count()#计算news和user都存在情况下计数，大于0就是存在了。
        print count
    if count > 0:
        data={}
        date['message']='您已投票'
        return JsonResponse(data)
    else:   
        update=Userlikes.objects.create(news=news,user=user)
        update.sava()
        news.poll_num+=1
        news.save()
        data={}
        date['message']='投票失败'
    return JsonResponse(data)

@login_required
def like_category(request):
    #context = RequestContext(request)
    cat_id = None
    likes = 0
    if request.method == 'GET':
        cat_id = request.GET['category_id']

        
        if cat_id:
            category = News.objects.get(id=int(cat_id))
            if category:
                likes = category.likes + 1
                category.likes = likes
                category.save()

    return HttpResponse(likes)
    
def search(request):
    #context = RequestContext(request)
    error=[]
    if request.method == 'GET':
        keyword=request.GET['keyword']
        if keyword:
            search_list=News.object.all().filter(Q(title__icontains=keywords) | Q(message__icontains=keywords))
            context_dict = {'search_list': search_list,'keyword':keyword}  
            print keyword,search_list
            return render(request, 'news/search.html', context_dict)
        else:
            error.append('请输入正确的关键词')
            context_dict = {'error': error}
            print error          
    return render(request, 'news/search.html', context_dict)
'''
def ajax_list(request):
    a = range(100)
    return jsonResponse(a, safe=False)

  '''

  
def tt(request):
    return render_to_response('news/add.html')
  
  
names=list();
names.append("zhangsa")
names.append("aa")
names.append("b")
names.append("c")
  
  
@csrf_exempt
def ccc(request):
    name=request.POST.get("name",None)
    rtxt="";
    if name is not None:
        b=name in names
        if b:
            rtxt="名字已经存在！"
        else:
            print("名字不存在!")
            rtxt="名字不存在!"
        #print("获取的名字是:NU",name) 
    return HttpResponse(json.dumps({"msg":rtxt})) 



    
    
        
