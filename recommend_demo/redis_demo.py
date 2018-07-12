#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= redis_demo
@author= wubingyu
@create_time= 2018/7/11 下午3:07
"""
import redis
import pymysql.cursors
import sys
import json
import itertools
import house

reload(sys)
sys.setdefaultencoding('utf8')


def rank(data):
	print data
	houses = json.loads(data)
	for object in houses:
		del object['lng']
		del object['lat']
	return json.dumps(houses, ensure_ascii=False)


def parse_json(data):
	datas = rank(data[3])
	return datas


if __name__ == '__main__':

	connect = pymysql.connect(host='192.168.10.221', port=3306, user='root', password='idontcare', database='crawl',
							  use_unicode=True, charset='utf8')

	cursor = connect.cursor()

	r = redis.Redis(host='192.168.10.221', port=6379)

	cursor.execute(' select * from xiaoqu limit 50')

	data = cursor.fetchall()

	for object in data:
		if object[2] != "null" and object[3] != 'null':
			print "***" + str(object)
			result = parse_json(object)
			r.set(object[1], result)
# r = redis.Redis(host='192.168.10.221', port=6379)
# print r.get("michael")
