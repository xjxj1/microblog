# -*- coding: utf-8 -*-
# @Time    : 2020-07-12 21:51
# @Author  : wxl
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'