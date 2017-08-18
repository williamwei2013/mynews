# -*- coding: utf-8 -*-
# 1.7django用这个 from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings 
from mynews import settings
from django.conf.urls import include, url
#from mynews import views
from django.views import static
from rest_framework.routers import DefaultRouter
from news.serializers import  *
from rest_framework import viewsets
from mynews import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)  
router.register(r'news', views.NewsViewSet)
#增加router路由。指向view中的viewset

urlpatterns = [
    # Examples:
    # url(r'^$', 'mynews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('news.urls')),#不去掉$,news下面的url都无法解析 #url(r'^/news/', include('news.urls')),
    #url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    url(r'^register/', views.register_view,name='register'),
    url(r'^login/', views.login_view,name='login'),
    url(r'^logout/', views.logout_view,name='logout'),
    url(r'^register_check/', views.register_check,name='register_check'),
    url(r'^register_demo/', views.register_demo,name='register_demo'),  
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^static/(?P<path>.*)$',static.serve, {'document_root':settings.STATIC_ROOT}, name='static'),#仅在本地测试使用，正式环境全部用nginx
    url(r'^media/(?P<path>.*)', static.serve,{'document_root': settings.MEDIA_ROOT},name='media' ),#上传文件
    url(r'^api/', include(router.urls)),   
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]