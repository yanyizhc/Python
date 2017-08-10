#coding:utf-8
# d = {}

# d['user'] = raw_input(">")
# d['pwd'] = raw_input(">")
# Game_user_txt = open("Gameuser.txt",'ab+')
# print d
# Game_user_txt.write(d)
import re 
import json



# a = "hash=adfadfasdfadf97adf"
# print re.findall(r'hash=(\w+)*', a)


# a = '''user:ff,pwd:ff
       # user:aaa,pwd:aa'''
#('ff', 'ff')
#('aaa', 'aa')	   
	   
# b = re.findall(r"user:(\w+),pwd:(\w+)",a)

# for i in range(len(b)):
	# for j in range(len(b[i])):
		# print "tuple  : %s %s" %(i,j)
		
		# a = b[i][j]
		# print " :",a
	# print 
	
user = raw_input(">")
pwd = raw_input(">")
# s = '{"user":'+ user +',"pwd":'+ pwd+'}' 
# json = json.loads(s)
# print json
s = '{"user":"'+ user +'","pwd":"'+ pwd +'"}' 
json = json.loads(s)

print json






















