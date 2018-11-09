from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    """
    课程表
    例如：
        Linux
        Python自动化精英
        Python全栈
    """
    title = models.CharField(verbose_name='课程名称', max_length=32)

    def __str__(self):
        return '{}'.format(self.title)


class ClassList(models.Model):
    """
    班级表
    """
    course = models.ForeignKey(verbose_name='课程', to='Course')
    num = models.IntegerField(verbose_name='第几期')
    teachers = models.ManyToManyField(verbose_name='老师', to='User')
    def __str__(self):
        return '{} {} {}'.format(self.course.title,self.num,self.teachers.name)
