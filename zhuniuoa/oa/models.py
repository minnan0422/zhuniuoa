from django.db import models
from users.models import User
from django.urls import  reverse
from django.utils.html import strip_tags
# Create your models here.



class Overtime_work(models.Model):

    body = models.CharField(max_length=999)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_time =  models.IntegerField()
    create_time = models.DateTimeField('创建时间',auto_now=True)
    oa_user = models.ForeignKey(User)


    def __int__(self):
        return self.oa_user

class Time_off(models.Model):

    body = models.CharField(max_length=999)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    off_time =  models.IntegerField()
    create_time = models.DateTimeField('创建时间',auto_now=True)
    oa_user = models.ForeignKey(User)

    def __int__(self):
        return self.oa_user

class Total_time(models.Model):
    total_time = models.IntegerField()
    oa_user = models.ForeignKey(User)

    def __int__(self):
        return self.total_time



