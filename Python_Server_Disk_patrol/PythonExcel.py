#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xlwt
import time
ISOTIMEFORMAT_t = '%Y%m%d-'

def excel_template():
    time.sleep(0.5)
    print '进入文件创建函数,执行中……'
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet('Sheet1')
    style = xlwt.XFStyle()
    # 为样式创建字体
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
    row_name_o = [u'地址', u'环境', u'查询时间', u'总大小(%)',u'是否清理']
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
    sheet.write_merge(5, 5, 0, 10)
    # 第一列
    # row_name_th = [u'163', u'132(YD)', u'133(YD)', u'164', u'183', u'194', u'155']
    # row_name_thx, row_name_thx_num = 2, 0
    # row_name_thx_positioning, while_initial_number = 5, 0
    # while while_initial_number <= len(row_name_th):
    #     if row_name_thx == row_name_thx_positioning:
    #         row_name_thx += 1
    #         while_initial_number += 1
    #         continue;
    #     else:
    #         sheet.write(row_name_thx, 0, row_name_th[row_name_thx_num],style)
    #         print "c===", row_name_thx
    #         row_name_thx += 1
    #         row_name_thx_num += 1
    #         while_initial_number += 1
    # print len(row_name_th)
    # sheet.write_merge(2, 4, 1, 1, excel_Style())
    # sheet.write_merge(6, len(row_name_th)+2, 1, 1, style)

    new_time = time.strftime(ISOTIMEFORMAT_t, time.localtime())
    file_te = r"C:\\Users\\Administrator\\Desktop\\"+new_time+"server.xls"

    wbk.save(file_te)
    time.sleep(0.5)
    print '文件创建成功，路径：%s' %(file_te)
    return file_te


file = excel_template()
print file
