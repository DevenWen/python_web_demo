#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/08/25 23:16:52
@Author  :   Liu YuanYuan :)
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("hello world, You're at the polls index.")