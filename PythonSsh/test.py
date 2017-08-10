#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding = utf-8
# serverOneIp = '192.168.133.133'
# serverOneuser = 'root'
# serverOnepwd = '12345678'
import json
import time
import chardet
ISOTIMEFORMAT_t = '-%Y%m%d'
#
# server_Data = '{"Serverlist": [{"Serverip": "192.168.133.133", "Serveruser": "root","Serverpwd": "12345678" },{"Serverip": "192.168.133.147","Serveruser": "root","Serverpwd": "171800" }]}'
# s = json.loads(server_Data)
# server_list = s['Serverlist']
# for a in server_list:
#     Serverip = a['Serverip']
#     serverOneIp = a['Serverip']
#     serverOneuser = a['Serveruser']
#     serverOnepwd = a['Serverpwd']
#     print serverOneIp
#     print serverOneuser
#     print serverOnepwd
#
# file_path = r"C:\Users\Administrator\Desktop\服务器磁盘大小巡查"
# new_time = time.strftime(ISOTIMEFORMAT_t, time.localtime())
# file_f = ".xls"
# file = file_path+new_time+file_f
# print file
#
# excel_data_list = []
# excel_data_list.insert(0, '1')
# excel_data_list.insert(1, '2')
# excel_data_list.insert(2, '3')
# excel_data_list.insert(3, '4')
#
# print len(excel_data_list)
#
# server_Data = '{"Server_excel_list": [{"Server_excel": "192.168.133.133", "excel_": 2 },{"Server_excel": "192.168.133.147", "excelnum": 3 }]}'
#
# if return_num == 3:
#     for SeExDaLists in SeExDaList:
#         Server_excel_ip = SeExDaLists['Server_excelip']
#         if serverOneIp == Server_excel_ip:
#             excelx = SeExDaLists['excel_num']
#             Server_environment = SeExDaLists['Server_environment']
#
#     excel_data_list = []
#     excel_data_list.insert(0, serverOneIp)
#     excel_data_list.insert(1, Server_environment)
#     excel_data_list.insert(2, new_time)
#     excel_data_list.insert(3, catil_tomcat_list[0])
#     excel_data_list.insert(4, '', )
#     excel_data_list.insert(5, soft_disk_tomcat_one_list[0])
#     excel_data_list.insert(6, soft_disk_tomcat_one_list[1])
#     excel_data_list.insert(7, soft_disk_tomcat_one_list[2])
#     excel_data_list.insert(8, soft_disk_tomcat_two_list[0])
#     excel_data_list.insert(9, soft_disk_tomcat_two_list[1])
#     excel_data_list.insert(10, soft_disk_tomcat_two_list[2])
#
#     excely = 0
#     list_num = 0
#     for ex_data in range(len(excel_data_list)):
#         sheet.write(excelx, excely, excel_data_list[list_num], style)
# #     excely += 1
# #     list_num += 1
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
# new_time = time.strftime(ISOTIMEFORMAT_t, time.localtime())
#
#
# # file_te = r'C:\\Users\\Administrator\\Desktop\\' + new_time +
# file_1 = "C:\\Users\\Administrator\\Desktop\\ "
# file_3 = r"server.xls"
# file_te = file_1 + new_time + file_3
#
# file_te5 = "中午呢"
# print file_te5
# fencoding4 = chardet.detect(file_1)
# print fencoding4
#
#
#         font1 = xlwt.Font()
#         font1.name = 'SimSun'
#         # 设置单元格对齐方式
#         alignment = xlwt.Alignment()
#         alignment.horz = xlwt.Alignment.HORZ_CENTER
#         alignment.vert = xlwt.Alignment.VERT_CENTER
#         # 单元格背景色  0x30 0x1E  0x28 [0x2C] 【0x34 0x16】
#         pattern_yellow = xlwt.Pattern()
#         pattern_yellow.pattern = xlwt.Pattern.SOLID_PATTERN
#         pattern_yellow.pattern_fore_colour = 0x16
#         # 设置单元格边框
#         borders = xlwt.Borders()
#         borders.right = xlwt.Borders.THIN
#         borders.left = xlwt.Borders.THIN
#         borders.top = xlwt.Borders.THIN
#         borders.bottom = xlwt.Borders.THIN
#         sheet.col(0).width = 5000
#         sheet.col(1).width = 2000
#         sheet.col(2).width = 5000
#         sheet.col(3).width = 5000
#         sheet.col(4).width = 2000
#         sheet.col(5).width = 3000
#         sheet.col(6).width = 3000
#         sheet.col(7).width = 3000
#         sheet.col(8).width = 3000
#         sheet.col(9).width = 3000
#         sheet.col(10).width = 3000
#         sheet.set_col_default_width(2)
#
#         style.font = font1
#         style.alignment = alignment
#         style.pattern = pattern_yellow
#         style.borders = borders
#         # excel创建格式
#         # 第一行
#         row_name_o = [u'地址', u'环境', u'查询时间', u'总大小(%)', u'是否清理']
#         row_name_ox, row_name_owy, row_name_o_num = 0, 0, 0
#         while row_name_ox < len(row_name_o) and row_name_owy <= len(row_name_o):
#             sheet.write_merge(0, 1, row_name_ox, row_name_owy, row_name_o[row_name_o_num], style)
#             row_name_ox += 1
#             row_name_owy += 1
#             row_name_o_num += 1
#         sheet.write_merge(0, 0, 5, 7, 'tomcat（1）', style)
#         sheet.write_merge(0, 0, 8, 10, 'tomcat（2）', style)
#
#         row_name_t = [u'端口号', u'项目名', u'大小(G)', u'端口号', u'项目名', u'大小(G)']
#         row_name_tx, row_name_t_num = 5, 0
#         while row_name_tx < 11:
#             sheet.write(1, row_name_tx, row_name_t[row_name_t_num], style)
#             row_name_tx += 1
#             row_name_t_num += 1
#         sheet.write_merge(5, 5, 0, 10)
#
#
#
# font1 = xlwt.Font()
#             font1.name = 'SimSun'
#             # 设置单元格对齐方式
#             alignment = xlwt.Alignment()
#             alignment.horz = xlwt.Alignment.HORZ_CENTER
#             alignment.vert = xlwt.Alignment.VERT_CENTER
#             # 设置单元格边框
#             borders = xlwt.Borders()
#             borders.right = xlwt.Borders.THIN
#             borders.left = xlwt.Borders.THIN
#             borders.top = xlwt.Borders.THIN
#             borders.bottom = xlwt.Borders.THIN
#             sheet.set_col_default_width(2)
#             style.font = font1
#             style.alignment = alignment
#             style.borders = borders
# list_o = ['1', 'zhangsan']
# list_t = ['2', 'lisi ']
# data_list = []
# for a in range(4):
#     data_list.append(list_o)
#
# print data_list
#
# excelx
#             excely = 0
#             final_value = 11
#             list_num = 0
#             list_num_2 = 0
#             for initial_value in final_value:
#                 print excelx, excely, list_num_2, list_num
#                 sheet.write(excelx, excely, server_data_list[list_num_2][list_num], style)
#                 excely += 1
#                 list_num += 1
#                 initial_value += 1
#                 list_num_2 += 1
Disk_alarm_value = 2.0
catil_tomcat_list = []
catil_Log_list = []
server_Data = {
    "Serverlist": [
        {
            "Serverip": "192.168.133.133",
            "Serveruser": "root",
            "Serverpwd": "12345678",
            "excel_num": 2,
            "Server_environment": "测试"
        },
        {
            "Serverip": "192.168.133.147",
            "Serveruser": "root",
            "Serverpwd": "171800",
            "excel_num": 2,
            "Server_environment": "测试"
        },
        {
            "Serverip": "192.168.133.134",
            "Serveruser": "root",
            "Serverpwd": "12345678",
            "excel_num": 2,
            "Server_environment": "测试"
        },
        {
            "Serverip": "192.168.133.135",
            "Serveruser": "root",
            "Serverpwd": "12345678",
            "excel_num": 2,
            "Server_environment": "测试"
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

df_h = [
    u'\u6587\u4ef6\u7cfb\u7edf                       \u5bb9\u91cf  \u5df2\u7528  \u53ef\u7528 \u5df2\u7528% \u6302\u8f7d\u70b9\n',
    u'/dev/mapper/centos_yanyi-root   46G   34G   15G   55% /\n',
    u'devtmpfs                       2.0G     0  2.0G    0% /dev\n',
    u'tmpfs                          2.0G     0  2.0G    0% /dev/shm\n',
    u'tmpfs                          2.0G  8.7M  2.0G    1% /run\n',
    u'tmpfs                          2.0G     0  2.0G    0% /sys/fs/cgroup\n',
    u'/dev/sda1                      497M  137M  361M   28% /boot\n',
    u'tmpfs                          394M     0  394M    0% /run/user/0\n',
    u'/dev/sdb1                      9.8G   23M  9.2G    1% /softwarelog\n']
cd_du = [u'5.5G\tapache-tomcat-8084\n', u'3G\tapache-tomcat-8028\n', u'5.2G\tapache-tomcat-8092\n',
                     u'4.3G\tapache-tomcat-8028\n', u'3.3G\tapache-tomcat-8122\n', u'2.2G\tapache-tomcat-8099\n']

def zhumain_cd_du(cd_du):
    time.sleep(0.5)
    catil_Log_one = ''.join(cd_du[0]).strip().lstrip().rstrip(',')
    catil_Log_two = ''.join(cd_du[1]).strip().lstrip().rstrip(',')

    # 1号数据处理流程
    # soft_disk_tomcat_one_size = float(catil_Log_one[0:3].rstrip('G'))
    # print soft_disk_tomcat_one_size
    # if soft_disk_tomcat_one_size >= Disk_alarm_value:
    #     time.sleep(0.5)
    #     soft_disk_tomcat_one_name = catil_Log_one[5:]
    #     soft_disk_tomcat_one_port = soft_disk_tomcat_one_name[-4:]
    #     # 通过端口号查询出项目中文名
    #     application_one_name = select_port_application(soft_disk_tomcat_one_port)
    #     # 将获取的端口号，项目中文名，应用大小添加到list中。
    #     soft_disk_tomcat_one_list.insert(0, soft_disk_tomcat_one_port)
    #     soft_disk_tomcat_one_list.insert(1, application_one_name)
    #     soft_disk_tomcat_one_list.insert(2, soft_disk_tomcat_one_size)
    #     whether_return_one = 1
    # else:
    #     time.sleep(0.5)
    #     whether_return_one = 2
    #     pass

    # 2号数据处理流程
    print catil_Log_one[0:3].rstrip('\t').rstrip('G')
    print catil_Log_two[0:3].rstrip('\t').rstrip('G')
    # soft_disk_tomcat_two_size = float(catil_Log_two[0:3].rstrip('G'))
    # print soft_disk_tomcat_two_size
    # if soft_disk_tomcat_two_size >= Disk_alarm_value:
    #     time.sleep(0.5)
    #     soft_disk_tomcat_two_name = catil_Log_two[5:]
    #     soft_disk_tomcat_two_port = soft_disk_tomcat_two_name[-4:]
    #     # 通过端口号查询出项目中文名
    #     application_two_name = select_port_application(soft_disk_tomcat_two_port)
    #     # 将获取的端口号，项目中文名，应用大小添加到list中。
    #     soft_disk_tomcat_two_list.insert(0, soft_disk_tomcat_two_port)
    #     soft_disk_tomcat_two_list.insert(1, application_two_name)
    #     soft_disk_tomcat_two_list.insert(2, soft_disk_tomcat_two_size)
    #     whether_return_two = 1
    # else:
    #     time.sleep(0.5)
    #     whether_return_two = 2
    #     pass
    # whether_return_state_list.insert(0, whether_return_one)
    # whether_return_state_list.insert(1, whether_return_two)
    # time.sleep(1)
    # return soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, whether_return_state_list

def zhumain_df_h(df_h):
    # 处理原始数据为使用数据
    time.sleep(0.5)
    catil_tomcat = ''.join(df_h[1]).strip().lstrip().rstrip()
    catil_tomcat_num = catil_tomcat.rsplit('G', 1)[-1].strip().lstrip().replace(' ', '').rstrip('% /')
    # catil_tomcat_name = catil_tomcat.rsplit('%', 1)[-1].strip().lstrip().rstrip()
    print catil_tomcat_num
    # print catil_tomcat_name

    # catil_Log = ''.join(df_h[4]).strip().lstrip().rstrip()
    # # 截取根目录
    # catil_tomcat_num = catil_tomcat.rsplit('G', 1)[-1].strip().lstrip().replace(' ', '').rstrip('% /')
    # catil_tomcat_name = catil_tomcat.rsplit('%', 1)[-1].strip().lstrip().rstrip()
    # # 将处理的数据添加到list中
    # catil_tomcat_list.insert(0, catil_tomcat_num)
    # catil_tomcat_list.insert(1, catil_tomcat_name)
    #
    # # 截取的log目录
    # catil_Log_num = catil_tomcat.rsplit('G', 1)[-1].strip().lstrip().rstrip('/')
    # catil_Log_name = catil_Log.rsplit('%', 1)[-1].strip().lstrip()
    # # 将处理的数据添加到list中
    # catil_Log_list.insert(0, catil_Log_num)
    # catil_Log_list.insert(1, catil_Log_name)
    # time.sleep(1)
    # return catil_tomcat_list, catil_Log_list

# 进入端口查询项目名称阶段
def select_port_application(soft_disk_tomcat_port):
    time.sleep(0.5)
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
    time.sleep(1)
    return projectname

# catil_tomcat_list, catil_Log_list = zhumain_df_h(df_h)
# print catil_tomcat_list, catil_Log_list
# soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, whether_return_state_list = zhumain_cd_du(cd_du)
# print soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, whether_return_state_list
# zhumain_df_h(df_h)
zhumain_cd_du(cd_du)