#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= pageRank_demo
@author= wubingyu
@create_time= 2018/7/9 下午4:06
"""
from pyspark import SparkContext, SparkConf

conf = SparkConf.setMaster("local").setAppName("PageRank")
sc = SparkContext(conf=conf)

links=sc.parallelize([['A', ['B', 'C']], ['B', ['A', 'C']], ['C', ['A', 'B', 'D']], ['D', ['C']]]).partitionBy(100).persist()

links.collect()

