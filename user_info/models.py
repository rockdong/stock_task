#_*_coding:utf-8_*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name='账号')
    mail = models.EmailField(verbose_name='邮箱')
