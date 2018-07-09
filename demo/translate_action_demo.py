#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= translate_action_demo
@author= wubingyu
@create_time= 2018/7/5 下午3:11
"""
from pyspark import SparkConf, SparkContext
import numpy as np
import itertools

conf = SparkConf().setMaster("local").setAppName("sparkconf")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(np.array(range(4)))

print rdd.sample(False, 0.8).collect()

print "****"

print rdd.flatMap(lambda x: itertools.combinations(x)).collect()
