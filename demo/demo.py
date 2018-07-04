#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= demo
@author= wubingyu
@create_time= 2018/6/15 上午10:06
"""
from pyspark.sql import SparkSession
import pyspark.sql.functions as psf

README_PATH = "/home/michael/spark/README.md"
# store the spark temp data
TEMP_PATH = "/home/michael/python_project/spark-demo/temp"


def demo():
	spark = SparkSession.builder.appName("michael's first application").getOrCreate()

	text_file = spark.read.text(README_PATH)

	print("count:%d" % text_file.count())

	print("first line:%s" % text_file.first())

	# text_file.filter(text_file.vgalue.contains("spark")).show()

	print(text_file.select(psf.size(psf.split(text_file.value, "\s+")).name("numWords")).agg(
		psf.max(psf.col("numWords"))).collect())

	word_counts = text_file.select(psf.explode(psf.split(text_file.value, "\s+")).name("word")).groupBy("word").count()

	print (word_counts.collect())

	rdd = spark.sparkContext.parallelize(range(1, 4)).map(lambda x: (x, "a" * x))

	rdd.saveAsSequenceFile(TEMP_PATH)

	print(sorted(spark.sparkContext.sequenceFile(TEMP_PATH).collect()))

	spark.stop()


if __name__ == '__main__':
	demo()
