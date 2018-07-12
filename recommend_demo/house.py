#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= house
@author= wubingyu
@create_time= 2018/7/11 下午4:09
"""


class house(object):
	def __int__(self, name, count):
		self.name = name
		self.count = count

	@property
	def name(self):
		return self.name

	@property
	def count(self):
		return self.count

	def __hash__(self):
		return super(house, self).__hash__()

	def __eq__(self, o):
		return super(house, self).__eq__(o)

	def __call__(self, *args, **kwargs):
		return 0
