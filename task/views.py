#_*_coding:utf-8_*_

from django.shortcuts import HttpResponse
from django.views.generic import View

import json
import tushare as ts

from stock.models import Stock

# Create your views here.


class UpdateStockView(View):
    '''
        更新数据库，如果有新的股票信息就更新。
    '''
    def get(self, request):
        stocks = ts.get_stock_basics()
        for code in stocks.index:
            print not Stock.objects.filter(code=code).exists()
            print Stock.objects.filter(code=code).exists()
            if not Stock.objects.filter(code=code).exists():
                stock = Stock()
                stock.code = code
                stock.save()
        return HttpResponse(json.dumps({"status": "success"}), content_type="application/json")


class UpdateDateInfoView(View):
    '''
        更新每天的股票信息，如果不存在该股票的信息，则更新日期从上市日到当天
    '''
    pass


class CalculateView(View):
    '''
        计算每个股票第二天的是否买入或者卖出
    '''
    pass


class NofifyView(View):
    '''
        发送邮件通知
    '''
    pass
