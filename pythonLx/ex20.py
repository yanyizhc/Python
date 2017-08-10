#coding:utf-8
from sys import argv
script , input_file = argv
#使用文件读取函数
def read_all(f):
	print f.read()
#回到文件内容开始函数
def rewind(f):
	f.seek(0)
#读取文件一行内容函数
def print_a_llne (cu_line, f):
	print cu_line, f.readline()

inpu_file = open(input_file)
print ".... : \n"
read_all(inpu_file)
rewind(inpu_file)

cu_line = 1 
print_a_llne(cu_line, inpu_file)

cu_line = cu_line + 1
print_a_llne(cu_line, inpu_file)

cu_line = cu_line + 1
print_a_llne(cu_line, inpu_file)

