#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/8

from django.shortcuts import redirect,render,HttpResponse
from study.models import Course
from study.forms.course import CourseModelForm
from study.utils.pager import Pagination
from study import models

def list(request):
    # my_list = Course.objects.all()
    page = request.GET.get('page', 1)  # 要查看的页码
    total_count = models.Course.objects.all().count()  # 数据库中数据总条数
    pager = Pagination(page, total_count, '/study/course/list/',1)
    my_list = models.Course.objects.all()[pager.start :pager.end]
    return render(request,'course/list.html',locals())


def login(request):
    title_login = "欢迎登陆"
    title_password = "密码"
    title_course = "用户名"
    form = CourseModelForm()
    if request.method == "POST":
        form = CourseModelForm(data=request.POST)
        if form.is_valid():
            return HttpResponse("登陆成功")
    return render(request,"course/login.html",locals())

def register(request):
    title_login = "欢迎注册"
    title_password = "密码"
    title_course = "用户名"
    form = CourseModelForm()
    if request.method == "GET":
        return render(request,"course/register.html",locals())
    else:
        form = CourseModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/study/course/list/')

        return render(request,"course/register.html",locals())

def edit(request,nid):
    obj = Course.objects.filter(id=nid).first()
    form = CourseModelForm(instance=obj)
    if request.method == "POST":
        form = CourseModelForm(data=request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/study/course/list/')
    return render(request,'course/edit.html',locals())

def delete(request,nid):
    Course.objects.filter(id=nid).delete()
    return redirect('/study/course/list/')
