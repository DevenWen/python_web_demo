#!/usr/bin/python3
# -*- coding:UTF-8 -*-
'''
 @AUTHOR: kangqiang.w :)
 @FILE: ~/learn/python_web_demo/ssh_test/ssh_color.py
 @DATE: 2020/09/18 周五
 @TIME: 11:31:27

# DESCRIPTION:
'''

from colorama import Fore, Back, Style

print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now!!")
