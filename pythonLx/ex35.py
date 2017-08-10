#coding:utf-8

'''
原始需求：
小游戏，输入密码用户名，正确进入游戏，错误重新登录，回答5道题目，
并且记录正确题目数以及错误题目数，
——————————————————————————————————————————————————————————————————————————
新增需求：
1、登录账号从文件中提取如果没有需要进行注册. Gameuser.txt
2、题目、答案从文件中提取. Gameproblem.txt
3、将游戏记录存储到文件中. 文件目录为：win C盘：PGame  PGameLog.txt
4、游戏界面 x
5、游戏测试 x
6、游戏打包 x
'''
import getpass
import time
import json

#小横线函数
def heng():
	print "-" * 50
	
#打开程序函数
def open_Game():
	print u""" 欢迎登录小游戏"""
	print u"""注册,请输入1"""
	print u"""登录,请输入2"""
	reg = raw_input(">")
	if reg == "1":
		print reg
		regis()
	elif reg == "2":
		log()
		raw_input()
		
#注册函数
def regis():
	print u"""欢迎来到pGame小游戏，请输入用户名和密码进行注册"""
	regisUser = raw_input(">regisUser: ")
	regisPwd = raw_input(">regisPwd: ")
	Game_user_txt = open("Gameuser.txt",'ab+')
	Game_user_txt.write(regisUser)
	Game_user_txt.write(",")
	Game_user_txt.write(regisPwd)
	Game_user_txt.write("\r\n")
	Game_user_txt.close()
	print u"注册成功"
	
#检测注册账号是否有重复
def regis_repeat():
	Gameuser_user_repeat = open("Gameuser.txt",'r')
	Gameuser_user_repeat_read = Gameuser_user_repeat.read()
	print Gameuser_user_repeat_read
	
		
	
#登录函数
def log():
	user = raw_input("> user: ")
	pwd = getpass.getpass("> pwd: ")
	if user == "zhc" and pwd =="zhc":
		print u"用户:%s, 登录成功！进入游戏" % user
	elif user == "admin" and pwd == "admin":
		print u"管理员: %s登录成功！进入游戏后台" % user
	else :
		print u"用户名密码错误，请重新启动该小游戏!"
		exit()

#问题函数
def problem_answer():
	pr1 = u"1、一年有多少个天？"
	an1_1 = u"A : 365 "
	an1_2 = u"B : 368 "
	pr2 = u"2、一年有多少个月？"
	an2_1 = u"A : 12 "
	an2_2 = u"B : 15 "
	pr3 = u"3、一个月有多少天？"
	an3_1 = u"A : 35 "
	an3_2 = u"B : 30 "
	pr4 = u"4、一天有多少小时？"
	an4_1 = u"A : 30 "
	an4_2 = u"B : 24 "
	pr5 = u"5、一小时有多少分钟？"
	an5_1 = u"A : 80 "
	an5_2 = u"B : 60 "
#参数
	correct_num = 0
	error_num = 0
#问题1处理
	print pr1
	print an1_1, an1_2
	pr1_answer = raw_input(">").upper()
	correct_answer = "A"
	if problem(pr1_answer,correct_answer):
		correct_num += 1
	else:
		error_num += 1
	
#问题2处理
	print pr2
	print an2_1, an2_2
	pr2_answer = raw_input(">").upper()
	correct_answer = "A"
	if problem(pr2_answer,correct_answer):
		correct_num += 1
	else:
		error_num += 1
#问题3处理
	print pr3
	print an3_1, an3_2
	pr3_answer = raw_input(">").upper()
	correct_answer = "B"
	if problem(pr3_answer,correct_answer):
		correct_num += 1
	else:
		error_num += 1

#问题4处理
	print pr4
	print an4_1, an4_2
	pr4_answer = raw_input(">").upper()
	correct_answer = "B"
	if problem(pr4_answer,correct_answer):
		correct_num += 1
	else:
		error_num += 1
#问题5处理
	print pr5
	print an5_1, an5_2
	pr5_answer = raw_input(">").upper()
	correct_answer = "B"
	if problem(pr5_answer,correct_answer):
		correct_num += 1
	else:
		error_num += 1
		
	print u" 回答完毕：\n 正确数: %s \n 错误数: %s " %(correct_num,error_num)
	
#问题判断处理
def problem(answer,correct_answer):
	if answer == correct_answer :
		return True
	else:
		return False
	
#总控函数
def boos_Game():
	heng()
	open_Game()
	#print u"回车进入游戏!"
	#problem_answer()
	#print u"游戏记录将记录在文档中，请xx文件中查看！"
	#print u"恭喜完成，5秒后游戏自动退出！"
	time.sleep(5)
	

#boos_Game()
#regis_repeat()
regis()


