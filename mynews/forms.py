# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    
class  RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email address'}),label=u'邮箱')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label=u'用户名')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label=u'密码')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label=u'确认密码')
