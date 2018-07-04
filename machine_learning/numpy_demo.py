#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= numpy_demo
@author= wubingyu
@create_time= 2018/7/4 上午10:35
"""
import numpy as np

a = [1, 2, 3, 4]
b = np.array(a)

print b.size
print b.ndim
print b.shape
print b.dtype

print np.zeros([10, 10])

print np.ones([10, 10])

print np.random.rand(10, 10)

print np.random.uniform(0, 100)

print np.random.randint(0, 100)

print np.random.normal(1.75, 0.1, (2, 3))

arr = np.random.normal(1.75, 0.1, (4, 5))
print arr

after_arr = arr[1:3, 2:4]
print after_arr

one_20 = np.ones([20])
print one_20

one_4_5 = one_20.reshape([4, 5])
print one_4_5

stut_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print stut_score > 80

print np.where(stut_score < 80, 0, 90)

print np.amax(stut_score, axis=0)

print np.amax(stut_score, axis=1)

print np.mean(stut_score, axis=0)

print np.mean(stut_score, axis=1)

print np.std(stut_score, axis=0)

print np.std(stut_score, axis=1)

stut_score[:, 0] = stut_score[:, 0] + 5
print stut_score

q = np.array([[0.4], [0.6]])

result = np.dot(stut_score, q)
print result
