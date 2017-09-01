#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# s = pd.Series([10, 20, 40, 30])
# print s
# 0    10
# 1    20
# 2    40
# 3    30
# dtype: int64

# dir = {"a": 1, "c": 2, "d": 3}
# dir_1 = pd.Series(dir)
# print dir_1
# a    1
# c    2
# d    3
# dtype: int64

# arr_ = np.arange(5, 10)
# s2 = pd.Series(arr_, index=list("abcde"))
# print s2
# a    5
# b    6
# c    7
# dtype: int32
# # print s2.index
# s2.index = ["aa", "bb", "cc", "dd", "ee"]
# s2.index.name = "zhc"
# s2.name = "fa"
# print s2
# print s2.values
# print s2["cc"]
# print s2["bb":"ee"]
# s2["ee"] = 100
# s2[1] = 15
# print s2
# s2["ff"] = 20
# s2["hh"] = 30
# # del s2["hh"]
# print s2 > 8
# print s2[s2 > 8]
# print s2[s2 == 9]
# print s2
#
# s = pd.Series([10, np.nan, 15, 20, None])
# # print s
# print s[~s.isnull()]
# print s.fillna(value=0)
# print s
# # print s.fillna(method="ffill")
#
# s3 = pd.Series([10, 15, 8, 15, 20], index=list("abdef"))
# # print s3
# # print s3.sort_index(ascending=False)
#
# s4 = pd.Series([100, 50, 100, 75, 24, 100])
# # print s4.describe().round()
#
# s5 = pd.Series([100, 50, 100, 75, 24, 100])
#
# s6 = pd.Series([50, 70, 80])
# s7 = pd.Series([20, 30])
# print s6 + s7
# dict_1 = pd.DataFrame({"a": range(100, 111), "b": range(200, 211)})
# print dict_1
# df2 = pd.Series(dict_1)
# dict_2 = {"a": {2015: 4, 2016: 5, 2017: 6}, "b": {2017: 27, 2016: 20, 2015: 10}}
# df2 = pd.DataFrame(dict_2)
# print df2

# dict_3 = {"b": {2015: 4, 2016: 5, 2017: 6}, "a": {2017: 27, 2016: 20, 2015: 10}}
# df3 = pd.DataFrame(dict_3)
# print df3
#
# df4 = pd.DataFrame(np.arange(12).reshape(3, 4), index=[1, 2, 3], columns=["a", "b", "c", "d"])
# print df4

cs_1 = pd.read_csv("pokemon_data.csv", encoding="gbk")
# print cs_1
# print cs_1.head()
# print cs_1.tail()
# print cs_1.columns
# print cs_1.index
# print cs_1.shape
# print cs_1.dtypes
# print cs_1.isnull().tail(20)
# print cs_1[cs_1[u"类型2"].isnull()]
# print cs_1[u"类型2"].unique()
# print cs_1[u"类型1"].value_counts()
# print cs_1

# print cs_1[u"类型2"].isnull().value_counts()
# print

# print len(cs_1[u"类型1"].value_counts())
# # 对数据进行拆分
# group_1 = cs_1.groupby(u"类型1")
# # 求均值
# print group_1[[u"攻击力"]].mean()
group_2 = cs_1.groupby([u"类型1", u"类型2"])
# print group_2[[u"攻击力"]].mean()
# print group_2[[u"攻击力"]].agg([np.mean, np.median, np.sum])
# print group_2.agg({u"攻击力":[np.mean, np.median], u"生命值": np.sum})
# print group_2.size()
# size_filter = lambda x: len(x) < 10
# print group_2.filter(size_filter)


# import numpy as np
# import matplotlib.pyplot as plt
# 饼图
# labels = 'frogs', 'hogs', 'dogs', 'logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)
#
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

# 直方图
# np.random.seed(0)
# mu, sigme = 100, 20
# a = np.random.normal(mu, sigme, size=100)
# plt.hist(a, 40, normed=0, histtype='stepfilled', facecolor='b', alpha=0.75)
# plt.title('Histogram')
# plt.show()

# 极坐标图
# n = 20
# theta = np.linspace(0.0, 2 * np.pi, n, endpoint=False)
# radii = 10 * np.random.rand(n)
# width = np.pi / 4 * np.random.rand(n)
#
# ax = plt.subplot(111, projection='polar')
# bars = ax.bar(theta, radii, width=width, bottom=0.0)
# for r, bar in zip(radii, bars):
#     bar.set_facecolor(plt.cm.viridis(r / 10.))
#     bar.set_alpha(0.5)
# plt.show()
#
# # 散点图
# fig, ax = plt.subplots()
# ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
# ax.set_title('Simple Scatter')
# plt.show()










