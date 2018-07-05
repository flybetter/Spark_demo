#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@project= Spark_demo
@file= matplotlib_demo_2
@author= wubingyu
@create_time= 2018/7/5 下午1:53
"""
import matplotlib.pyplot as plt
import random
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 条形图绘制名侦探柯南主要角色年龄
role_list = ["michael", "sdsds", "sdasd", "ffff", "gggg", "bbb", "nnn", "lll"]
role_age = [7, 17, 7, 34, 32, 30, 27, 46]
# 实际年龄
role_ture_age = [18, 17, 18, 34, 45, 30, 27, 46]

x = [i + 1 for i, role in enumerate(role_list)]

y = role_age
y2 = role_ture_age

plt.figure(figsize=(15, 8), dpi=100)

plt.bar(x, y, width=-0.4, label="role age", color="#509839")
plt.bar(x, y2, width=0.3, label="role real age", color="#c03035")

x_desc = [_ for _ in role_list]

plt.xticks(x, x_desc)

y = range(50)[::5]

plt.yticks(y)

plt.xlabel("role")
plt.ylabel("age")
plt.title("the role in cartoon Detective conan")
plt.legend(loc="best")

plt.show()
