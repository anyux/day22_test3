#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "anyux"
# Date: 2018/11/8

from django.conf.urls import url
from study.views import user
from study.views import course
from study.views import classList

urlpatterns = [
    # 用户
    url(r'^login/', user.login),
    url(r'^register/', user.register),
    url(r'^user/list/', user.list),
    url(r'^user/edit/(\d+)', user.edit),
    url(r'^user/delete/(\d+)', user.delete),
    # 课程
    url(r'^course/register/', course.register),
    url(r'^course/list/', course.list),
    url(r'^course/edit/(\d+)', course.edit),
    url(r'^course/delete/(\d+)', course.delete),
    #班级
    url(r'^class/register/', classList.register),
    url(r'^class/list/', classList.list),
    url(r'^class/edit/(\d+)', classList.edit),
    url(r'^class/delete/(\d+)', classList.delete),
]
