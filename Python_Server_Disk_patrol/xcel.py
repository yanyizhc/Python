#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlutils.copy import copy
from xlwt import Style
# file = r'D:\python Text\pythonEx\test.xls'

# op_file = xlrd.open_workbook(file, formatting_info=True)
# table = op_file.sheet_by_index(1)
# wbk = xlwt.Workbook()
# she = wbk.add_sheet('zfdfdfd', cell_overwrite_ok=True)
# she.write(0, 0, 'fffffff')
# wbk.save(file)
#
# def writeExcel(row, col, str, styl=Style.default_style):
#     rb = xlrd.open_workbook(file, formatting_info=True)
#     wb = copy(rb)
#     ws = wb.get_sheet(0)
#     ws.write(row, col, str, styl)
#     wb.save(file)
#
#
# style = xlwt.easyxf('font:height 240, color-index red, bold on;align: wrap on, vert centre, horiz center');
# writeExcel(1, 2, 'hello wfforld', style)


import _winreg
def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,\
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return _winreg.QueryValueEx(key, "Desktop")[0]


print get_desktop()