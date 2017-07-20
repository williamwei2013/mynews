# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from news.views import *
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mynews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name='index'),
    url(r'^news/about/$', views.about,name='about'),
    url(r'^news/article_detail/(?P<id>\d+)/$', views.article_detail,name='article_detail'),
    url(r'^news/click_like/(?P<id>\d+)/$',views.click_like,name='click_like'),
    url(r'^news/like_category/$', views.like_category, name='like_category'),
    url(r'^news/search/$', views.search, name='search'),
)
