# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class News(models.Model):
    author = models.CharField(u'作者',max_length=500)
    title= models.CharField(u'标题',max_length=500,)
    message=RichTextField()
    publish_date=models.DateTimeField(auto_now_add=True)#
    update_time = models.DateTimeField(auto_now=True, null=True)
    published = models.BooleanField('notDraft', default=True)
    likes = models.IntegerField(default=0)  
    
    def __unicode__(self):
        return self.title



        
class Userlikes(models.Model):
    user = models.ForeignKey(User)
    news = models.ForeignKey(News)
    status=models.BooleanField(default=1)
    like_time = models.DateTimeField(auto_now=True, null=True)
    
    def __unicode__(self):
        return self.news.title
        
        
class Zxfc(models.Model):
    title= models.CharField(u'标题',max_length=500,)
    time= models.DateTimeField()
    url=models.CharField(u'链接',max_length=500,)
    
    def __unicode__(self):
        return self.title
        
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture= models.ImageField(u'头像',upload_to='profile_images', blank=True,)
    intro=models.CharField(u'链接',max_length=500,blank=True)
    
    def __unicode__(self):
        return self.user.username
        


 