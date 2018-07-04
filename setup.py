#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= setup
@author= wubingyu
@create_time= 2018/6/19 下午2:06
"""
from setuptools import setup

setup(
	name='Spark_demo',
	version='1.0.0',
	install_requires=[
		"py4j==0.10.7",
		"pyspark==2.3.1"
	]
)
