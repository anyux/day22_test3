#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/4


from django.forms import ModelForm
from django import forms
from study import models

class CourseModelForm(ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"
        widgets = {
            'title' : forms.TextInput(attrs = {
                'class':'form-control',
                'placeholder':models.Course._meta.fields[1].verbose_name
            }),
        }
        error_messages = {
            'name' : {
                'required':'用户名不能为空'
            },

        }
