# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.decorators import detail_route
from models import *
from rest_framework import viewsets

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'message', 'publish_date', 'update_time','published','likes')

        
class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ('url', 'username', 'email')
