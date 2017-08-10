#!/usr/bin/env python
# -*- coding:utf-8 -*-
import paramiko
import time
import os
import chardet
import xlwt
import json
import xlrd
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 变量定义
catil_tomcat_list = []
catil_Log_list = []
soft_disk_tomcat_one_list = []
soft_disk_tomcat_two_list = []
excel_data_list = []
whether_return_state_list = []

# 当前时间格式
Disk_alarm_value = 2.0
ISOTIMEFORMAT_SHEET = '%Y%m%d'
ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
ISOTIMEFORMAT_t = '%m%d-'
ISOTIMEFORMAT_m = '%H:%M'
now_time = time.strftime(ISOTIMEFORMAT, time.localtime())

return_state = 1
server_Data = {
    "Serverlist": [
        {
            "Serverip": "192.168.133.133",
            "Serveruser": "root",
            "Serverpwd": "12345678",
            "excel_num": 3,
            "Server_environment": "测试"
        },
        {
            "Serverip": "192.168.133.147",
            "Serveruser": "root",
            "Serverpwd": "171800",
            "excel_num": 5,
            "Server_environment": "生产"
        },
        {
            "Serverip": "192.168.133.134",
            "Serveruser": "root",
            "Serverpwd": "12345678",
            "excel_num": 4,
            "Server_environment": "测试"
        },
        {
            "Serverip": "192.168.133.135",
            "Serveruser": "root",
            "Serverpwd": "12345678",
            "excel_num": 6,
            "Server_environment": "生产"
        },
    ],
    "applicationlist": [
        {
            "portId": 8114,
            "projectName": "联通"
        },
        {
            "portId": 8099,
            "projectName": "宝安"
        },
        {
            "portId": 8081,
            "projectName": "SAP推送"
        },
        {
            "portId": 8092,
            "projectName": "VP下发"
        },
        {
            "portId": 8084,
            "projectName": "直送单下发"
        },
        {
            "portId": 8090,
            "projectName": "SAP回传"
        },
        {
            "portId": 8091,
            "projectName": "CPWEB"
        },
        {
            "portId": 8070,
            "projectName": "辉瑞"
        },
        {
            "portId": 8122,
            "projectName": "用友"
        },
        {
            "portId": 8115,
            "projectName": "红星美凯龙"
        },
        {
            "portId": 8080,
            "projectName": "铁塔"
        },
        {
            "portId": 8020,
            "projectName": "阿里巴巴"
        },
        {
            "portId": 8041,
            "projectName": "河南政采"
        },
        {
            "portId": 8095,
            "projectName": "华为"
        },
        {
            "portId": 8045,
            "projectName": "工商银行"
        }
    ]
}
server_list = server_Data['Serverlist']

def heng():
    print "-" * 100
# 判断服务器是否正常
def pingServer(server):
    result = os.system('ping ' + server)
    if result:
        print u'服务器 ping fail'
        return 2
    else:
        print u'服务器 ping ok'
        return 1
    # print df_h, cd_du
    # print catil_tomcat_num, catil_tomcat_name, catil_Log_num, catil_Log_name
    # print soft_disk_tomcat_size, soft_disk_tomcat_name, soft_disk_tomcat_name_port
    # login_status = 1
    # if login_status == 1:
    #     time.sleep(1)
    #     print u'连接正常！'
    # else:
    #     time.sleep(1)
    #     print u'登录失败，请查找原因。'

def main():
    start = time.clock()
    server_List_num = 0
    a = 0
    server_data_list = []
    heng()
    print time.strftime('%Y-%m-%d %H:%M:%S')
    for server_List in server_list:
        Serverip = server_List['Serverip']
        serverOneIp = server_List['Serverip']
        serverOneuser = server_List['Serveruser']
        serverOnepwd = server_List['Serverpwd']

        # 返回未处理list数据
        # df_h, cd_du = command_returns(serverOneIp, serverOneuser, serverOnepwd)
        if a == 0:
            df_h = [
                u'\u6587\u4ef6\u7cfb\u7edf                       \u5bb9\u91cf  \u5df2\u7528  \u53ef\u7528 \u5df2\u7528% \u6302\u8f7d\u70b9\n',
                u'/dev/mapper/centos_yanyi-root   46G   10G   34G   20% /\n',
                u'devtmpfs                       2.0G     0  2.0G    0% /dev\n',
                u'tmpfs                          2.0G     0  2.0G    0% /dev/shm\n',
                u'tmpfs                          2.0G  8.7M  2.0G    1% /run\n',
                u'tmpfs                          2.0G     0  2.0G    0% /sys/fs/cgroup\n',
                u'/dev/sda1                      497M  137M  361M   28% /boot\n',
                u'tmpfs                          394M     0  394M    0% /run/user/0\n',
                u'/dev/sdb1                      9.8G   23M  9.2G    1% /softwarelog\n']
            cd_du = [u'4.5G\tapache-tomcat-8084\n', u'3G\tapache-tomcat-8028\n', u'5.2G\tapache-tomcat-8092\n',
                     u'4.3G\tapache-tomcat-8028\n', u'3.3G\tapache-tomcat-8122\n', u'2.2G\tapache-tomcat-8099\n']
            a += 1
        elif a == 1:
            df_h = [
                u'\u6587\u4ef6\u7cfb\u7edf                       \u5bb9\u91cf  \u5df2\u7528  \u53ef\u7528 \u5df2\u7528% \u6302\u8f7d\u70b9\n',
                u'/dev/mapper/centos_yanyi-root   46G   23G   23G   50% /\n',
                u'devtmpfs                       2.0G     0  2.0G    0% /dev\n',
                u'tmpfs                          2.0G     0  2.0G    0% /dev/shm\n',
                u'tmpfs                          2.0G  8.7M  2.0G    1% /run\n',
                u'tmpfs                          2.0G     0  2.0G    0% /sys/fs/cgroup\n',
                u'/dev/sda1                      497M  137M  361M   28% /boot\n',
                u'tmpfs                          394M     0  394M    0% /run/user/0\n',
                u'/dev/sdb1                      9.8G   23M  9.2G    1% /softwarelog\n']
            cd_du = [u'5.5G\tapache-tomcat-8055\n', u'5.4G\tapache-tomcat-8114\n', u'5.2G\tapache-tomcat-8091\n',
                     u'4.3G\tapache-tomcat-8028\n', u'3.3G\tapache-tomcat-8122\n', u'2.2G\tapache-tomcat-8099\n']
            a += 1
        elif a == 2:
            df_h = [
                u'\u6587\u4ef6\u7cfb\u7edf                       \u5bb9\u91cf  \u5df2\u7528  \u53ef\u7528 \u5df2\u7528% \u6302\u8f7d\u70b9\n',
                u'/dev/mapper/centos_yanyi-root   46G   34G   13G   80% /\n',
                u'devtmpfs                       2.0G     0  2.0G    0% /dev\n',
                u'tmpfs                          2.0G     0  2.0G    0% /dev/shm\n',
                u'tmpfs                          2.0G  8.7M  2.0G    1% /run\n',
                u'tmpfs                          2.0G     0  2.0G    0% /sys/fs/cgroup\n',
                u'/dev/sda1                      497M  137M  361M   28% /boot\n',
                u'tmpfs                          394M     0  394M    0% /run/user/0\n',
                u'/dev/sdb1                      9.8G   23M  9.2G    1% /softwarelog\n']
            cd_du = [u'10G\tapache-tomcat-8182\n', u'7.4G\tapache-tomcat-8092\n', u'5.2G\tapache-tomcat-8091\n',
                     u'4.3G\tapache-tomcat-8028\n', u'3.3G\tapache-tomcat-8122\n', u'2.2G\tapache-tomcat-8099\n']
            a += 1
        elif a == 3:
            df_h = [
                u'\u6587\u4ef6\u7cfb\u7edf                       \u5bb9\u91cf  \u5df2\u7528  \u53ef\u7528 \u5df2\u7528% \u6302\u8f7d\u70b9\n',
                u'/dev/mapper/centos_yanyi-root   46G   34G   5G   95% /\n',
                u'devtmpfs                       2.0G     0  2.0G    0% /dev\n',
                u'tmpfs                          2.0G     0  2.0G    0% /dev/shm\n',
                u'tmpfs                          2.0G  8.7M  2.0G    1% /run\n',
                u'tmpfs                          2.0G     0  2.0G    0% /sys/fs/cgroup\n',
                u'/dev/sda1                      497M  137M  361M   28% /boot\n',
                u'tmpfs                          394M     0  394M    0% /run/user/0\n',
                u'/dev/sdb1                      9.8G   23M  9.2G    1% /softwarelog\n']
            cd_du = [u'15G\tapache-tomcat-8090\n', u'9G\tapache-tomcat-8080\n', u'5.2G\tapache-tomcat-8091\n',
                     u'4.3G\tapache-tomcat-8028\n', u'3.3G\tapache-tomcat-8122\n', u'2.2G\tapache-tomcat-8099\n']
            a += 1

        # 返回已处理list数据
        time.sleep(1)
        catil_tomcat_list, catil_Log_list = zhumain_df_h(df_h)
        soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, whether_return_state_list = zhumain_cd_du(cd_du)
        time.sleep(1)
        server_List_num += 1
        server_list_data = data_excel(catil_tomcat_list, soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, serverOneIp)
        if server_list_data is None:
            pass
        else:
            server_data_list.append(server_list_data)
    time.sleep(1)
    file_te = inst_excel(server_data_list, server_List_num)
    time.sleep(1)
    print '文件保存地址：', file_te
    print ''
    end = time.clock()
    print u'完成！'
    print u'脚本运行时间：%s s' % (end - start)
    print u'完成时间：', now_time
# 命令结果返回函数
def command_returns(serverOneIp, serverOneuser, serverOnepwd):
        ps = paramiko.SSHClient()
        ps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ps.connect(hostname=serverOneIp, port=22, username=serverOneuser, password=serverOnepwd)
        commlistDf = ['df -h']
        for comm in commlistDf:
            stdin, stdout, stderr = ps.exec_command(comm)
            df_h = stdout.readlines()
        commlistDf = ['cd /soft \n du -sh *|sort -rh']
        for comm in commlistDf:
            stdin, stdout, stderr = ps.exec_command(comm)
            cd_du = stdout.readlines()
        ps.close()
        return df_h, cd_du

# df_h数据处理流
def zhumain_df_h(df_h):
        # 处理原始数据为使用数据
        catil_tomcat = ''.join(df_h[1]).strip().lstrip().rstrip()
        catil_Log = ''.join(df_h[4]).strip().lstrip().rstrip()
        # 截取根目录
        catil_tomcat_num = catil_tomcat.rsplit('G', 1)[-1].strip().lstrip().replace(' ', '').rstrip('% /')
        catil_tomcat_name = catil_tomcat.rsplit('%', 1)[-1].strip().lstrip().rstrip()
        # 将处理的数据添加到list中
        catil_tomcat_list.insert(0, catil_tomcat_num)
        catil_tomcat_list.insert(1, catil_tomcat_name)
        # 截取的log目录
        catil_Log_num = catil_tomcat.rsplit('G', 1)[-1].strip().lstrip().rstrip('/')
        catil_Log_name = catil_Log.rsplit('%', 1)[-1].strip().lstrip()
        # 将处理的数据添加到list中
        catil_Log_list.insert(0, catil_Log_num)
        catil_Log_list.insert(1, catil_Log_name)
        return catil_tomcat_list, catil_Log_list

# cd_du数据处理流
def zhumain_cd_du(cd_du):
    catil_Log_one = ''.join(cd_du[0]).strip().lstrip().rstrip(',')
    catil_Log_two = ''.join(cd_du[1]).strip().lstrip().rstrip(',')
    # 1号数据处理流程
    soft_disk_tomcat_one_size = float(catil_Log_one[0:3].rstrip('\t').rstrip('G'))
    if soft_disk_tomcat_one_size >= Disk_alarm_value:
        soft_disk_tomcat_one_name = catil_Log_one[5:]
        soft_disk_tomcat_one_port = soft_disk_tomcat_one_name[-4:]
        # 通过端口号查询出项目中文名
        application_one_name = select_port_application(soft_disk_tomcat_one_port)
        # 将获取的端口号，项目中文名，应用大小添加到list中。
        soft_disk_tomcat_one_list.insert(0, soft_disk_tomcat_one_port)
        soft_disk_tomcat_one_list.insert(1, application_one_name)
        soft_disk_tomcat_one_list.insert(2, soft_disk_tomcat_one_size)
        whether_return_one = 1
    else:
        whether_return_one = 2
        pass
    # 2号数据处理流程
    soft_disk_tomcat_two_size = float(catil_Log_two[0:3].rstrip('\t').rstrip('G'))
    if soft_disk_tomcat_two_size >= Disk_alarm_value:
        soft_disk_tomcat_two_name = catil_Log_two[5:]
        soft_disk_tomcat_two_port = soft_disk_tomcat_two_name[-4:]
        # 通过端口号查询出项目中文名
        application_two_name = select_port_application(soft_disk_tomcat_two_port)
        # 将获取的端口号，项目中文名，应用大小添加到list中。
        soft_disk_tomcat_two_list.insert(0, soft_disk_tomcat_two_port)
        soft_disk_tomcat_two_list.insert(1, application_two_name)
        soft_disk_tomcat_two_list.insert(2, soft_disk_tomcat_two_size)
        whether_return_two = 1
    else:
        whether_return_two = 2
        pass
    whether_return_state_list.insert(0, whether_return_one)
    whether_return_state_list.insert(1, whether_return_two)
    return soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, whether_return_state_list

# 进入端口查询项目名称阶段
def select_port_application(soft_disk_tomcat_port):
    # 进入端口查询项目名称阶段
    projectname = ''
    datalist = server_Data["applicationlist"]
    for e in datalist:
        # print soft_disk_tomcat_port
        f = e['portId']
        soft_disk_tomcat_port = int(soft_disk_tomcat_port)
        if soft_disk_tomcat_port == f:
            # print True
            projectname = e['projectName']
            break
        else:
            # print False
            projectname = 'null'
            pass
    return projectname

# 数据是否符合要求
def data_excel(catil_tomcat_list, soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, serverOneIp):
    server_list_data = [ ]
    catil_tomcat_size = int(catil_tomcat_list[0])
    # 如果应用目录使用百分比大于70进行数据写入excel
    if catil_tomcat_size >= 50:
        server_list_data.insert(0, serverOneIp)
        Serverlist = server_Data['Serverlist']
        for a in Serverlist:
            Serverip = a['Serverip']
            if serverOneIp == Serverip:
                Server_environment = a['Server_environment']
                server_list_data.insert(1, Server_environment)
        server_list_data.insert(2, now_time)
        server_list_data.insert(3, catil_tomcat_list[0])
        server_list_data.insert(4, '')
        server_list_data.insert(5, soft_disk_tomcat_one_list[0])
        server_list_data.insert(6, soft_disk_tomcat_one_list[1])
        server_list_data.insert(7, soft_disk_tomcat_one_list[2])
        server_list_data.insert(8, soft_disk_tomcat_two_list[0])
        server_list_data.insert(9, soft_disk_tomcat_two_list[1])
        server_list_data.insert(10, soft_disk_tomcat_two_list[2])
        print '巡查服务器编号：'+ serverOneIp + u' 符合录入要求'
        return server_list_data
    else:
        server_list_data.insert(0, serverOneIp)
        Serverlist = server_Data['Serverlist']
        for a in Serverlist:
            Serverip = a['Serverip']
            if serverOneIp == Serverip:
                Server_environment = a['Server_environment']
                server_list_data.insert(1, Server_environment)
        server_list_data.insert(2, now_time)
        server_list_data.insert(3, catil_tomcat_list[0])
        server_list_data.insert(4, '')
        server_list_data.insert(5, '')
        server_list_data.insert(6, '')
        server_list_data.insert(7, '')
        server_list_data.insert(8, '')
        server_list_data.insert(9, '')
        server_list_data.insert(10, '')
        print '巡查服务器编号：' + serverOneIp + u' 不符合录入要求'
        return server_list_data

# 写入excel文件
def inst_excel(server_data_list, server_List_num):
        wbk = xlwt.Workbook(encoding='utf-8')
        new_time = time.strftime(ISOTIMEFORMAT_SHEET, time.localtime())
        sheet = wbk.add_sheet(new_time, cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        font1 = xlwt.Font()
        font1.name = 'SimSun'
        # 设置单元格对齐方式
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        alignment.vert = xlwt.Alignment.VERT_CENTER
        # 单元格背景色  0x30 0x1E  0x28 [0x2C] 【0x34 0x16】
        pattern_yellow = xlwt.Pattern()
        pattern_yellow.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern_yellow.pattern_fore_colour = 0x16
        # 设置单元格边框
        borders = xlwt.Borders()
        borders.right = xlwt.Borders.THIN
        borders.left = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        sheet.col(0).width = 5000
        sheet.col(1).width = 2000
        sheet.col(2).width = 5000
        sheet.col(3).width = 5000
        sheet.col(4).width = 2000
        sheet.col(5).width = 3000
        sheet.col(6).width = 3000
        sheet.col(7).width = 3000
        sheet.col(8).width = 3000
        sheet.col(9).width = 3000
        sheet.col(10).width = 3000
        sheet.set_col_default_width(2)

        style.font = font1
        style.alignment = alignment
        style.pattern = pattern_yellow
        style.borders = borders
        # excel创建格式
        # 第一行
        row_name_o = [u'地址', u'环境', u'查询时间', u'总大小(%)', u'是否清理']
        row_name_ox, row_name_owy, row_name_o_num = 0, 0, 0
        while row_name_ox < len(row_name_o) and row_name_owy <= len(row_name_o):
            sheet.write_merge(0, 1, row_name_ox, row_name_owy, row_name_o[row_name_o_num], style)
            row_name_ox += 1
            row_name_owy += 1
            row_name_o_num += 1
        sheet.write_merge(0, 0, 5, 7, 'tomcat（1）', style)
        sheet.write_merge(0, 0, 8, 10, 'tomcat（2）', style)

        row_name_t = [u'端口号', u'项目名', u'大小(G)', u'端口号', u'项目名', u'大小(G)']
        row_name_tx, row_name_t_num = 5, 0
        while row_name_tx < 11:
            sheet.write(1, row_name_tx, row_name_t[row_name_t_num], style)
            row_name_tx += 1
            row_name_t_num += 1
        try:
            # 为样式创建字体
            style = xlwt.XFStyle()
            font1 = xlwt.Font()
            font1.name = 'SimSun'
            # 设置单元格对齐方式
            alignment = xlwt.Alignment()
            alignment.horz = xlwt.Alignment.HORZ_CENTER
            alignment.vert = xlwt.Alignment.VERT_CENTER
            # 设置单元格边框
            borders = xlwt.Borders()
            borders.right = xlwt.Borders.THIN
            borders.left = xlwt.Borders.THIN
            borders.top = xlwt.Borders.THIN
            borders.bottom = xlwt.Borders.THIN
            sheet.set_col_default_width(2)
            style.font = font1
            style.alignment = alignment
            style.borders = borders
            time.sleep(3)
            excelx = 2
            list_num_2 = 0
            for a in range(len(server_list)): # 4
                for_num = 11
                excely = 0
                list_num = 0
                data = server_data_list[list_num_2]
                for c in range(for_num):
                    sheet.write(excelx, excely, data[list_num], style)
                    excely += 1
                    list_num += 1
                list_num_2 += 1
                excelx += 1
            if server_List_num == len(server_list):
                new_time = time.strftime(ISOTIMEFORMAT_t, time.localtime())
                file_te = r"C:\\Users\\Administrator\\Desktop\\" + new_time + "server.xls"
                file_path = os.path.exists(file_te)
                if file_path == True:
                    print u'原文件已存在,修改文件名称!'
                    num = 1
                    str_num = str(num + 1)
                    file_te = r"C:\\Users\\Administrator\\Desktop\\" + new_time + r"server-" + str_num + r".xls"
                    num += 1
                    wbk.save(file_te)
                    print u'修改文件并录入成功！'
                    return file_te
                else:
                    wbk.save(file_te)
                    print u'录入文件成功！'
                    return file_te
        except UnboundLocalError:
            print u'局部变量的引用赋值前<文件>'
main()
