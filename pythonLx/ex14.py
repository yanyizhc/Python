#coding:utf-8
# 简单的问题答题，总共5道题目
# 引包
from sys import argv
script, user_name = argv
# ————————————————————————————————————————
# 参数
prompt = '>'

print u"你好 %s ，欢迎来到练习题 %s ," %(user_name, script)
print u"""
简单的问题，请进行答题，总体数：5道
"""
print u"接下来我们进入问答题吧！"
print "-" * 30
print u"问题1 : %s, 一年中有多少天？" % user_name
ok1 = raw_input(prompt)

print u"问题2 : %s, 一个月中有多少天？" % user_name
ok2 = raw_input(prompt)

print u"问题3 : %s, 一个天中有多少小时？" % user_name
ok3 = raw_input(prompt)

print u"问题4 : %s, 一小时中有多少分？" % user_name
ok4 = raw_input(prompt)

print u"问题5 : %s, 一分钟中有多少秒？" % user_name
ok5 = raw_input(prompt)

print u"一年有",ok1,u"天,"u"一个月有",ok2,u"天,"u"一天有",ok3,u"小时,"u"一小时有",ok4,u"分,"u"一分钟有",ok5,u"秒。"
