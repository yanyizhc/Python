#coding:utf-8
def one (*args):
	arg1, arg2 = args
	print "one-arg1 : %s, arg2 : %s  :" % (arg1, arg2)
	
def one1 (arg1 ,arg2):
	print "one1-arg1 : %s, arg2 : %s" % (arg1, arg2)
	
def one2 (arg1):
	print "one2-arg1 : %s " % arg1
	
def one3 ():
	print "one3-66666!"
	

one ("zhc","abc")
one1("123","456")
one2("789")
one3()