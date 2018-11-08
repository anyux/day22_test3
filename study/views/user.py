from django.shortcuts import redirect,render,HttpResponse
from study.models import User
from study.forms.user import UserModelForm
from study.utils.pager import Pagination
from study import models

def list(request):
    # my_list = User.objects.all()
    page = request.GET.get('page', 1)  # 要查看的页码
    total_count = models.User.objects.all().count()  # 数据库中数据总条数
    pager = Pagination(page, total_count, '/study/user/list/',1)
    my_list = models.User.objects.all()[pager.start :pager.end]
    return render(request,'user/list.html',locals())


def login(request):
    title_login = "欢迎登陆"
    title_password = "密码"
    title_user = "用户名"
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            return HttpResponse("登陆成功")
    return render(request,"user/login.html",locals())

def register(request):
    title_login = "欢迎注册"
    title_password = "密码"
    title_user = "用户名"
    form = UserModelForm()
    if request.method == "GET":
        return render(request,"user/register.html",locals())
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/study/user/list/')

        return render(request,"user/register.html",locals())

def edit(request,nid):
    obj = User.objects.filter(id=nid).first()
    form = UserModelForm(instance=obj)
    if request.method == "POST":
        form = UserModelForm(data=request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/study/user/list/')
    return render(request,'user/edit.html',locals())

def delete(request,nid):
    User.objects.filter(id=nid).delete()
    return redirect('/study/user/list/')