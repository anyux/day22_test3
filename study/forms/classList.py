#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/4


from django.forms import ModelForm
from django import forms
from study import models

class ClassListModelForm(ModelForm):
    class Meta:
        model = models.ClassList
        fields = "__all__"
        widgets = {
            'course' : forms.Select(attrs = {
                'class':'form-control',
                'placeholder':"课程",
            }),
            'teachers' : forms.Select(attrs={
                'class':'form-control',
                'placeholder':"教师",
            }),
            'num' : forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':"第几期",
            }),
        }
        error_messages = {
            'course' : {
                'required':'用户名不能为空'
            },

        }
