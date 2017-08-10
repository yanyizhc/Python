#coding:utf-8
#加
def add(a, b):
	return a + b
#减
def subtract(a, b):
	return a - b
#乘
def multiply(a, b):
	return a * b
#除
def divide(a, b):
	return a / b
	
add1 = add(1,5)
subtract1 = subtract(9,5)
multiply1 = multiply(5,5)
divide1 = divide(9,3)

print add1
print subtract1
print multiply1
print divide1

#14+5*8/2 = 34
wah = add(divide(multiply(5,8),2),14)
print wah