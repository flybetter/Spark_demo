#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= accumulater_demo
@author= wubingyu
@create_time= 2018/7/10 上午11:23
"""
from pyspark import SparkContext, SparkConf
from demo import README_PATH, TEMP_PATH
import os

conf = SparkConf().setMaster("local[*]").setAppName("accumulater")
sc = SparkContext(conf=conf)

file = sc.textFile(README_PATH)
# 创建Accumulator[Int]初始化为0
blankLines = sc.accumulator(0)


def extractcallsigns(line):
	global blankLines
	if line == "":
		blankLines += 1
	return line.split(" ")


callSigns = file.flatMap(extractcallsigns)
callSigns.saveAsTextFile(TEMP_PATH + os.sep + 'callsigns')

print("Blank lines:%d" % blankLines.value)
