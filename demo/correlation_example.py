#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= correlation_example
@author= wubingyu
@create_time= 2018/7/4 下午2:58
"""
from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation

from pyspark.sql import SparkSession

if __name__ == '__main__':
	spark = SparkSession.builder.appName("micheal's first app").getOrCreate()
	# data = [(Vectors.sparse(4, [(0, 1.0), (3, -2.0)]),),
	# 		(Vectors.dense([4.0, 5.0, 0.0, 3.0]),),
	# 		(Vectors.dense([6.0, 7.0, 0.0, 8.0]),),
	# 		(Vectors.sparse(4, [(0, 9.0), (3, 1.0)]),)]

	data = [[Vectors.dense([5.0, 3.0, 2.5])],
			[Vectors.dense([2.0, 2.5, 5.0])]]

	df = spark.createDataFrame(data, ["features"])
	r1 = Correlation.corr(df, "features").head()
	print("Pearson correlation matrix:\n" + str(r1[0]))

	r2 = Correlation.corr(df, "features", "spearman").head()
	print("Spearman correlation matrix:\n" + str(r2[0]))
	# $example off$

	spark.stop()
