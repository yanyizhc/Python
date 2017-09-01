#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:YanYi
# version:1.0
#
import paramiko
import time
import os
import xlwt
import sys
import _winreg
reload(sys)
sys.setdefaultencoding('utf-8')
# 变量定义
catil_tomcat_list = []
catil_Log_list = []
soft_disk_tomcat_one_list = []
soft_disk_tomcat_two_list = []
excel_data_list = []

# 当前时间格式
Disk_alarm_value = 3.0
ISOTIMEFORMAT_SHEET = '%Y%m%d'
ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
ISOTIMEFORMAT_t = '%m%d-'
ISOTIMEFORMAT_m = '%H:%M'
now_time = time.strftime(ISOTIMEFORMAT, time.localtime())
return_state = 1

server_Data = {
    "Serverlist": [
        {
            "Serverip": "10.78.1.163",
            "Serveruser": "root",
            "Serverpwd": "Staples_dev",
            "excel_num": 3,
            "Server_environment": "测试"
        },
        {
            "Serverip": "10.78.1.164",
            "Serveruser": "root",
            "Serverpwd": "Staples_app",
            "excel_num": 4,
            "Server_environment": "生产"
        },
        {
            "Serverip": "10.78.1.183",
            "Serveruser": "root",
            "Serverpwd": "Staples_ser",
            "excel_num": 5,
            "Server_environment": "生产"
        },
        {
            "Serverip": "10.10.2.155",
            "Serveruser": "root",
            "Serverpwd": "Staples_1",
            "excel_num": 6,
            "Server_environment": "生产"
        },
        {
            "Serverip": "10.78.1.194",
            "Serveruser": "root",
            "Serverpwd": "Staples_1",
            "excel_num": 7,
            "Server_environment": "生产"
        },
        {
            "Serverip": "10.78.3.202",
            "Serveruser": "root",
            "Serverpwd": "Staples_yd",
            "excel_num": 8,
            "Server_environment": "生产"
        },
        {
            "Serverip": "172.19.120.219",
            "Serveruser": "root",
            "Serverpwd": "Staples_yd",
            "excel_num": 9,
            "Server_environment": "生产"
        },
        {
            "Serverip": "172.19.120.218",
            "Serveruser": "root",
            "Serverpwd": "Staples_yd",
            "excel_num": 10,
            "Server_environment": "生产"
        },
        {
            "Serverip": "172.19.120.220",
            "Serveruser": "root",
            "Serverpwd": "Staples_yd",
            "excel_num": 11,
            "Server_environment": "生产"
        },
        {
            "Serverip": "172.19.120.221",
            "Serveruser": "root",
            "Serverpwd": "Staples_yd",
            "excel_num": 12,
            "Server_environment": "生产"
        }
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
        },
{
            "portId": 8025,
            "projectName": "国网"
        }
    ]
}

server_list = server_Data['Serverlist']

def heng():
    print "-" * 60
# 判断服务器是否正常
def pingServer(server):
    result = os.system('ping ' + server)
    if result:
        print u'服务器 ping fail'
        return 2
    else:
        print u'服务器 ping ok'
        return 1

def main():
    start = time.clock()
    time.sleep(0.2)
    print u'服务器巡查程序启动'
    server_List_num = 0
    server_data_list = []
    heng()
    time.sleep(0.2)
    print u'当前时间：', time.strftime('%Y-%m-%d %H:%M:%S')
    time.sleep(0.3)
    for server_List in server_list:
        serverOneIp = server_List['Serverip']
        serverOneuser = server_List['Serveruser']
        serverOnepwd = server_List['Serverpwd']
        # 返回未处理list数据
        # try:
        df_h, cd_du = command_returns(serverOneIp, serverOneuser, serverOnepwd)
        output = u'巡查服务器编号：%s ' % (serverOneIp)
        print output,
        time.sleep(0.5)
        print u'登录正常',
        time.sleep(1)
        catil_tomcat_list, catil_Log_list = zhumain_df_h(df_h)
        soft_disk_tomcat_one_list, soft_disk_tomcat_two_list = zhumain_cd_du(cd_du)
        server_List_num += 1
        server_list_data = data_excel(catil_tomcat_list, soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, serverOneIp)
        if server_list_data is None:
            pass
        else:
            server_data_list.append(server_list_data)
        print u'...',
        time.sleep(0.5)
        print u'巡查完毕'
        # except :
        #     print u'巡查异常'
        #     pass


    time.sleep(1)
    file_te = inst_excel(server_data_list, server_List_num)
    time.sleep(1)
    print u'文件保存地址：', file_te
    print ''
    end = time.clock()
    time.sleep(1)
    print u'服务器巡查程序终止！'
    print u'服务器巡查完成！'
    print ''
    time.sleep(0.2)
    print u'脚本运行时间：%s s' % (end - start)
    print u'完成时间：', now_time
    os.system(u"pause")
# 命令结果返回函数
def command_returns(serverOneIp, serverOneuser, serverOnepwd):
        ps = paramiko.SSHClient()
        ps.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ps.connect(hostname=serverOneIp, port=22, username=serverOneuser, password=serverOnepwd)
        commlistDf = ['df -h']
        time.sleep(1)
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
        # 截取根目录
        server_num_name = catil_tomcat[35:-1]
        catil_tomcat_num = catil_tomcat.rsplit(' ', 6)[5]
        catil_tomcat_name = catil_tomcat.rsplit(' ', 6)[6].strip().lstrip().rstrip()
        # 将处理的数据添加到list中
        catil_tomcat_list.insert(0, catil_tomcat_num)
        catil_tomcat_list.insert(1, catil_tomcat_name)
        # 截取的log目录
        catil_Log_num = catil_tomcat.rsplit('G', 1)[-1].strip().lstrip().rstrip('/')
        # 将处理的数据添加到list中
        catil_Log_list.insert(0, catil_Log_num)
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
    else:
        soft_disk_tomcat_one_list.insert(0, '')
        soft_disk_tomcat_one_list.insert(1, '')
        soft_disk_tomcat_one_list.insert(2, '')
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
    else:
        # 将获取的端口号，项目中文名，应用大小添加到list中。
        soft_disk_tomcat_two_list.insert(0, '')
        soft_disk_tomcat_two_list.insert(1, '')
        soft_disk_tomcat_two_list.insert(2, '')
    return soft_disk_tomcat_one_list, soft_disk_tomcat_two_list

# 进入端口查询项目名称阶段
def select_port_application(soft_disk_tomcat_port):
    # 进入端口查询项目名称阶段
    projectname = ''
    datalist = server_Data["applicationlist"]
    try:
        for e in datalist:
            # print soft_disk_tomcat_port
            f = e['portId']
            if soft_disk_tomcat_port == 'hnzc':
                projectname = '河南政采'
            elif soft_disk_tomcat_port == 'lete':
                projectname = '国网删除'
            else:
                soft_disk_tomcat_port = int(soft_disk_tomcat_port)
                if soft_disk_tomcat_port == f:
                    # print True
                    projectname = e['projectName']
                    break
                else:
                    # print False
                    projectname = 'null'
                    pass
    except ValueError:
        projectname = 'null'
    return projectname

# 数据是否符合要求
def data_excel(catil_tomcat_list, soft_disk_tomcat_one_list, soft_disk_tomcat_two_list, serverOneIp):
    server_list_data = [ ]
    catil_tomcat_size = int(catil_tomcat_list[0].rsplit('%')[0])
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
        # 单元格背景色  0x30 0x1E  0x28 [0x2C] 【0x16】
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
            for a in range(len(server_list)):
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
                Desktop = get_desktop()
                file_te = Desktop + r"\T-" + new_time + r"server_checks.xls"
                file_path = os.path.exists(file_te)
                if file_path == True:
                    print u'原文件已存在,修改文件名称!'
                    num = 1
                    str_num = str(num + 1)
                    file_te = Desktop + r"\T-" + new_time + r"server_checks-" + str_num + r".xls"
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
# 获取当前桌面路径
def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,\
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return _winreg.QueryValueEx(key, "Desktop")[0]

main()
