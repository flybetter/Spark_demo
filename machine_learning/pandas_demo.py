#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= pandas_demo
@author= wubingyu
@create_time= 2018/7/4 下午2:19
"""
import pandas as pd
import numpy as np
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

print  pd.Series(np.arange(4, 10))

data_3_4 = pd.DataFrame(np.arange(10, 22).reshape(3, 4))

print data_3_4

print data_3_4[:1]
print data_3_4[0]

result = pd.read_csv('./students_score.csv')

print result.shape

print result.dtypes
# 维度
print result.ndim

print result.index

print result.columns

print result.values

print result.head(5)

print result.tail(5)

print result.describe()

IMDB_100 = pd.read_csv("./IMDB-Movie-Data.csv", names=['Rating'])

print IMDB_100

print IMDB_100.sort_values(by="Rating", ascending=False)

print '*****'
print IMDB_100[3:4]

print IMDB_100.dropna()

print IMDB_100["Revenue (Millions)"].fillna(IMDB_1000["Revenue (Millions)"].mean(), inplace=True)