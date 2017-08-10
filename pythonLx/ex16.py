#coding:utf-8
#引包
from sys import argv
script, filename = argv

prompt = ">"
#读写文件
#读取文件内容
txt = open(filename)
txt_read = txt.read()
print txt_read
print "-" * 30
raw_input(prompt)
#写入文件内容 - 打开文件
file_w = open(filename , 'w')
#写入文件内容 - 清空文件内容
file_w.truncate()
#写入文件内容 - 添加文件内容
print u"写入文件内容1……"
w_1 = raw_input("w_1 : ")
print u"写入文件内容2……"
w_2 = raw_input("w_2 : ")
print u"写入文件内容3……"
w_3 = raw_input("w_3 : ")
print u"写入完成！存入文件中……"
file_w.write(w_1)
file_w.write("\n")
file_w.write(w_2)
file_w.write("\n")
file_w.write(w_3)
file_w.write("\n")
print u"存入成功"
#写入文件内容 - 关闭文件
file_w.close()
raw_input(prompt)
#读取文件内容
print u"读取文件内容"
txt = open(filename)
print txt.read()
print u"读取完成"
raw_input(prompt)
txt.close()

#关闭文件