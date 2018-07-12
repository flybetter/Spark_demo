#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= recommend_demo
@author= wubingyu
@create_time= 2018/7/12 上午9:58
"""
import requests
import json
import cx_Oracle


def get_recommand_block(url):
	data = json.loads(requests.get(url).text)
	print data
	print data['status']

	if data['status'] == 0:
		data = data['pois']
		print map(lambda x: x['blockName'] if x['isValidHouse'] == '1' else None, data)


if __name__ == '__main__':
	# url = 'http://tuijianapiv2.house365.com/analysis/getData?cityKey=nj&userId=13357732653&dataType=accesslog&pageSize=20&pageNum=1'
	# get_recommand_block(url)
	con = cx_Oracle.connect('app/app@202.102.83.165/app')
	print con.Version
