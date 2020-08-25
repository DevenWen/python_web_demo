#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   urls.py
@Time    :   2020/08/25 23:18:28
@Author  :   Liu YuanYuan :)
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]