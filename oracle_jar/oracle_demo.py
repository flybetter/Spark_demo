#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= oracle_demo
@author= wubingyu
@create_time= 2018/7/12 下午1:38
"""
import cx_Oracle

connection = cx_Oracle.connect('app/app@202.102.83.165/app')
print connection.version








