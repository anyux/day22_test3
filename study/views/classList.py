#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/8

from django.shortcuts import redirect,render,HttpResponse
from study.models import ClassList
from study.forms.classList import ClassListModelForm
from study.utils.pager import Pagination
from study import models

def list(request):
    # my_list = ClassList.objects.all()
    page = request.GET.get('page', 1)  # 要查看的页码
    total_count = models.ClassList.objects.all().count()  # 数据库中数据总条数
    pager = Pagination(page, total_count, '/study/class/list/',1)
    my_list = models.ClassList.objects.all()[pager.start :pager.end]
    return render(request,'class/list.html',locals())


def login(request):
    title_login = "欢迎登陆"
    title_password = "密码"
    title_class = "用户名"
    form = ClassListModelForm()
    if request.method == "POST":
        form = ClassListModelForm(data=request.POST)
        if form.is_valid():
            return HttpResponse("登陆成功")
    return render(request,"class/login.html",locals())

def register(request):
    title_login = "欢迎注册"
    title_password = "密码"
    title_class = "用户名"
    form = ClassListModelForm()
    if request.method == "GET":
        return render(request,"class/register.html",locals())
    else:
        form = ClassListModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/study/class/list/')

        return render(request,"class/register.html",locals())

def edit(request,nid):
    obj = ClassList.objects.filter(id=nid).first()
    form = ClassListModelForm(instance=obj)
    if request.method == "POST":
        form = ClassListModelForm(data=request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/study/class/list/')
    return render(request,'class/edit.html',locals())

def delete(request,nid):
    ClassList.objects.filter(id=nid).delete()
    return redirect('/study/class/list/')
