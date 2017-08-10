#coding:utf-8
#读取文件
#引包
from sys import argv
script, username = argv

print u"%s，请输入打开的文件名！" % username
file_name = raw_input(">")

open_txt = open(file_name)

print open_txt.read()
open_txt.close()
print u"文件关闭"