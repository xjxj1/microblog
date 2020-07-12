# -*- coding: utf-8 -*-
# @Time    : 2020-07-11 22:40
# @Author  : wxl
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


from app import routes