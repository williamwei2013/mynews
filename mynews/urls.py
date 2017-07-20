# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from mynews.views import *
#import xadmin
#xadmin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mynews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
    url(r'^', include('news.urls')),#不去掉$,news下面的url都无法解析
    #url(r'^/news/', include('news.urls')),
    url(r'^register/', 'mynews.views.register_view',name='register'),
    url(r'^login/', 'mynews.views.login_view',name='login'),
    url(r'^logout/', 'mynews.views.logout_view',name='logout'),
)