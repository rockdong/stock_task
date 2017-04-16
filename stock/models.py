# _*_coding:utf-8_*_

from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率
class Stock(models.Model):
    code = models.CharField(max_length=10, verbose_name='机构代码')


class DateInfo(models.Model):
    stock = models.ForeignKey(Stock, verbose_name='机构')
    date = models.DateField(verbose_name='日期')
    open = models.FloatField(verbose_name='开盘价')
    high = models.FloatField(verbose_name='最高价')
    close = models.FloatField(verbose_name='收盘价')
    low = models.FloatField(verbose_name='最低价')
    volume = models.IntegerField(verbose_name='成交量')
    change = models.FloatField(verbose_name='价格变动')
    applies = models.FloatField(verbose_name='涨跌幅')
    five_avg_price = models.FloatField(verbose_name='5日均价')
    ten_avg_price = models.FloatField(verbose_name='10日均价')
    twenty_avg_price = models.FloatField(verbose_name='20日均价')
    five_ave_volume = models.FloatField(verbose_name='5日均量')
    ten_avg_volume = models.FloatField(verbose_name='10日均量')
    twenty_avg_volume = models.FloatField(verbose_name='20日均量')
    turnover_rate = models.FloatField(verbose_name='换手率')
