# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from news.models import *


    
class  UserprofileForm(forms.ModelForm):  
    class Meta:
        model = UserProfile
        fields = ('picture', 'intro',)