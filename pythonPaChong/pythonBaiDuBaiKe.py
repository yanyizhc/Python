#coding:utf-8
#爬取 python 百科数据
from bs4 import BeautifulSoup
import urllib
import urllib2
import re

def url_Download(url):
	html = urllib2.urlopen(url).read()
	
	soup = BeautifulSoup(html, "html.parser")
	
	soup_div = soup.find('div',attrs={'class':'col-lg-9 col-md-8 col-sm-8 col-xs-12'})
	
		

	
	
url='https://www.aqistudy.cn/historydata/monthdata.php?city=上海'
url_Download(url)

