#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= pageRank_demo
@author= wubingyu
@create_time= 2018/7/9 下午4:06
"""
from __future__ import division
from pyspark import SparkContext, SparkConf


def compute(object):
	pageId = object[0]
	links = object[1][0]
	rank = object[1][1]
	return map(lambda a: (a, rank / len(links)), links)


if __name__ == '__main__':
	conf = SparkConf().setMaster("local").setAppName("PageRank")
	sc = SparkContext(conf=conf)

	links = sc.parallelize([['A', ['B', 'C']], ['B', ['A', 'C']], ['C', ['A', 'B', 'D']], ['D', ['C']]]).partitionBy(
		100).persist()

	ranks = links.map(lambda x: (x[0], 1))

	for _ in range(2):
		contributes = links.join(ranks).flatMap(compute)
		ranks = contributes.reduceByKey(lambda x, y: x + y).mapValues(lambda x: 0.15 + 0.85 * x)

	print contributes.collect()
	print ranks.sortByKey().collect()
	print links.collect()
