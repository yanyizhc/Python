#!/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
import getpass
import datetime
def heng():
    print "-" * 50
# 选择服务器函数
def serverlist():
    print u'请输入服务器ip：'
    sshid = raw_input('>')
    print u'请输入服务器用户名：'
    sshusr = raw_input('>')
    print u'请输入服务器密码：'
    sshpwd = getpass.getpass('>')
    return sshid,sshusr,sshpwd


def tombir(tomcatnum,dir,execute_command):
    cd = 'cd /soft/apache-tomcat-' + tomcatnum + '/' + dir
    if tomcatnum == "1":
        commlistC = [cd + ' \n ' + execute_command]
        print ' --' + tomcatnum
        print  commlistC
    elif tomcatnum == '2':
        commlistC = [cd + '\n' + execute_command]
    elif tomcatnum == '3':
        commlistC = [cd + '\n' + execute_command]
    elif tomcatnum == '4':
        commlistC = [cd + '\n' + execute_command]
    elif tomcatnum == '5':
        commlistC = [cd + '\n' + execute_command]
        print commlistC
    return commlistC
#指令拼接函数
def command(commandf):
    if commandf == "1":
        commlistC = ['df -h']
    elif commandf == "2":
        commlistC = ['cd /soft \n du -sh *|sort -sh  ']
    elif commandf == "3":
        #  参数1：tomcat 编号 参数2：bin
        print u'停止指定tomcat'
        print u'请输入指定的tomcat编号：'
        print u'1、tomcat-1 \t 2、tomcat-2 \t 3、tomcat-3 \t 4、tomcat-4 \t 5、tomcat-5'
        tomcatnum = raw_input('>')
        execute_command= './shutdown.sh'
        dir = "bin"
        commlistC = tombir(tomcatnum,dir,execute_command)
    elif commandf == "4":
        #  参数1：tomcat 编号 参数2：logs
        print u'指定日志文件改名-l'
        print u'请输入指定的tomcat编号：'
        print u'1、tomcat-1 \t 2、tomcat-2 \t 3、tomcat-3 \t 4、tomcat-4 \t 5、tomcat-5'
        tomcatnum = raw_input('>')
        cur = datetime.datetime.now()
        month = cur.strftime('%m')
        day = cur.strftime('%d')
        execute_command = 'mv catalina.out catalina'+ month + day + '.out'
        print execute_command
        dir = "logs"
        commlistC = tombir(tomcatnum, dir,execute_command)

    elif commandf == "5":
        #  参数1：tomcat 编号 参数2：bin
        print u'启动指定tomcat'
        print u'请输入指定的tomcat编号：'
        print u'1、tomcat-1 \t 2、tomcat-2 \t 3、tomcat-3 \t 4、tomcat-4 \t 5、tomcat-5'
        tomcatnum = raw_input('>')
        execute_command = './startup.sh'
        dir = "bin"
        commlistC = tombir(tomcatnum,dir,execute_command)
    elif commandf == "6":
        #  参数1：tomcat 编号 参数2：logs
        print u'指定日志备份'
        print u'请输入指定的tomcat编号：'
        print u'1、tomcat-1 \t 2、tomcat-2 \t 3、tomcat-3 \t 4、tomcat-4 \t 5、tomcat-5'
        tomcatnum = raw_input('>')
        cur = datetime.datetime.now()
        month = cur.strftime('%m')
        day = cur.strftime('%d')
        cd = '../../../softwarelog/2017/'+month + '/'+ day
        execute_command = 'mv catalina'+month+day+'.out '+ cd
        dir = "logs"
        commlistC = tombir(tomcatnum, dir,execute_command)
    elif commandf == "7":
        #  参数1：tomcat 编号 参数2：logs
        print u'指定tomcat日志输出'
        print u'请输入指定的tomcat编号：'
        print u'1、tomcat-1 \t 2、tomcat-2 \t 3、tomcat-3 \t 4、tomcat-4 \t 5、tomcat-5'
        tomcatnum = raw_input('>')
        execute_command = 'tail catalina.out'
        dir = "logs"
        commlistC = tombir(tomcatnum, dir,execute_command)
    return commlistC

#命令执行函数
def server_perform(sshid, sshusr, sshpwd):
    paramiko.util.log_to_file("paramiko.log")
    ps = paramiko.SSHClient()
    ps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ps.connect(hostname=sshid, port=22, username=sshusr, password=sshpwd)
    print u'进入执行命令区间:'
    print u'1、查询当前内存 \n2、查询soft目录下各tomcat占用大小 \n3、停止指定tomcat\n4、指定日志文件改名备份\n' \
          u'5、启动指定tomcat\n6、指定日志备份\n7、指定tomcat日志输出'
    commandf = raw_input('>')
    commlistC = command(commandf)

    for comm in commlistC:
        stdin, stdout, stderr = ps.exec_command(comm)
        out = stdout.readlines()
        for o in out:
            print o
    ps.close()


heng()
sshid, sshusr, sshpwd = serverlist()

# 主函数
def main_zhu(sshid, sshusr, sshpwd):
    server_perform(sshid, sshusr, sshpwd)
i = 0
while True:
    if i > 0:
        print u'输入任意字符并回车继续，输入大写ESC退出'
        raw = raw_input(">")
        if raw !="ESC":
            main_zhu(sshid, sshusr, sshpwd)
        else:
            exit()
    elif True:
        main_zhu(sshid, sshusr, sshpwd)
        i += 1





