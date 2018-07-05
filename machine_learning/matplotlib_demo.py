#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= matplotlib_demo
@author= wubingyu
@create_time= 2018/7/5 上午10:35
"""
import matplotlib.pyplot as plt
import random

# plt.plot([1, 2, 3, 4])
# plt.ylabel("some numbers")
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.show()

beijing_x = [_ for _ in range(0, 24)]
beijing_y = [random.randint(10, 30) for _ in range(0, 24)]

plt.plot(beijing_x, beijing_y, label="beijing")

shanghai_x = [_ for _ in range(0, 24)]
shanghai_y = [random.randint(10, 20) for _ in range(0, 24)]

plt.plot(shanghai_x, shanghai_y, label="shanghai")

hefei_x = [_ for _ in range(0, 24)]
hefei_y = [random.randint(30, 40) for _ in range(0, 24)]

plt.plot(hefei_x, hefei_y, label="hefei", color="#823384", linestyle=":", linewidth=3, alpha=0.3)

##坐标轴

x_ = [x_ for x_ in range(24)]
x_desc = ["{}h".format(_) for _ in x_]

plt.xticks(x_, x_desc)

y_ = [_ for _ in range(50)][::2]
y_desc = ["{}c".format(_) for _ in y_]

plt.yticks(y_, y_desc)

plt.xlabel("time")
plt.ylabel("temperature")

plt.title("the temperature change in one day")

plt.legend(loc="best")

plt.show()
