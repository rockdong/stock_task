# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='\u65e5\u671f')),
                ('open', models.FloatField(verbose_name='\u5f00\u76d8\u4ef7')),
                ('high', models.FloatField(verbose_name='\u6700\u9ad8\u4ef7')),
                ('close', models.FloatField(verbose_name='\u6536\u76d8\u4ef7')),
                ('low', models.FloatField(verbose_name='\u6700\u4f4e\u4ef7')),
                ('volume', models.IntegerField(verbose_name='\u6210\u4ea4\u91cf')),
                ('change', models.FloatField(verbose_name='\u4ef7\u683c\u53d8\u52a8')),
                ('applies', models.FloatField(verbose_name='\u6da8\u8dcc\u5e45')),
                ('five_avg_price', models.FloatField(verbose_name='5\u65e5\u5747\u4ef7')),
                ('ten_avg_price', models.FloatField(verbose_name='10\u65e5\u5747\u4ef7')),
                ('twenty_avg_price', models.FloatField(verbose_name='20\u65e5\u5747\u4ef7')),
                ('five_ave_volume', models.FloatField(verbose_name='5\u65e5\u5747\u91cf')),
                ('ten_avg_volume', models.FloatField(verbose_name='10\u65e5\u5747\u91cf')),
                ('twenty_avg_volume', models.FloatField(verbose_name='20\u65e5\u5747\u91cf')),
                ('turnover_rate', models.FloatField(verbose_name='\u6362\u624b\u7387')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='\u673a\u6784\u4ee3\u7801')),
                ('name', models.CharField(max_length=100, verbose_name='\u673a\u6784\u540d\u79f0')),
            ],
        ),
        migrations.AddField(
            model_name='dateinfo',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock', verbose_name='\u673a\u6784'),
        ),
    ]
