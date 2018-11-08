#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/4


from django.forms import ModelForm
from django import forms
from study import models

class UserModelForm(ModelForm):
    class Meta:
        model = models.User
        fields = "__all__"
        widgets = {
            'name' : forms.TextInput(attrs = {
                'class':'form-control',
                'placeholder':models.User._meta.fields[1].verbose_name
            }),
            'password' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':models.User._meta.fields[2].verbose_name
            }),
        }
        error_messages = {
            'name' : {
                'required':'用户名不能为空'
            },
            'password':{
                'required':'密码不能为空'
            }

        }
