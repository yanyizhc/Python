#coding:utf-8
#读取文件
#引包
from sys import argv
script, filename = argv

txt = open(filename)
print u"文件名叫：%s" % filename

print u"文件内容如下：" , txt.read()

