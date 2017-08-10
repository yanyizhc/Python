# coding:utf-8
from sys import argv
#从 ex17_text.txt 复制内容到ex17_text2.txt
from os.path import exists

script, from_file, to_file = argv

print u"复制 %s 内容到 %s" %(from_file, to_file)
in_file = open(from_file)
indata  = in_file.read()


#print "ex17_text: $s" % exists(to_file)

raw_input()

to_file = open(to_file , 'w')
to_file.write(indata)
print u"复制完成"

in_file.close()
to_file.close()
