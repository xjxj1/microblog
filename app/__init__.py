# -*- coding: utf-8 -*-
# @Time    : 2020-07-11 22:40
# @Author  : wxl
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)


from app import routes