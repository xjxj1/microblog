# -*- coding: utf-8 -*-
# @Time    : 2020-07-11 22:44
# @Author  : wxl
# @Site    : 
# @File    : routes.py
# @Software: PyCharm

from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!!'

