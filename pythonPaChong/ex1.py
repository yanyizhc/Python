#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import re
import itertools
from bs4 import BeautifulSoup
#
def download(url,user_agent='wswp',num_retries=2):
	headers = {'User-agent':user_agent}
	request = urllib2.Request(url,headers=headers)
	try:
		html= urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		html = None
		if num_retries > 0 :
			if hasattr(e,'code') and 500<= e.code < 600:
				return download(url, user_agent, num_retries)
	return html
		
def downloadf(url):
	sitemap = download(url)
	links = re.findall('<loc>(.*?)</loc>',sitemap)
	for link in links:
		html = download(link)
	  
# downloadf('http://example.webscraping.com/sitemap.xml')

# for page in itertools.count(1):
	# print page
	# url = 'http://example.webscraping.com/view/-%d' % page
	# html = download(url)
	# print html
	# if html is None:
		# break 
	# else:
		# pass
		
		
# url = 'http://example.webscraping.com/view/Afghanistan-1'
# html = download(url)
# print re.findall('><tr id="places_area__row"><td class="w2p_fl"><label for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>',html)

# broken_html = '<ul class=country><li>Area<li>Population</ul>'
# soup = BeautifulSoup(broken_html,'html.parser')
# fixed_heml = soup.prettify()
# print fixed_heml
# ul = soup.find('ul' ,attrs ={'class':'country'})
# print ul.find('li')
# print ul.find_all('li')

# def crawl(url):
    # page = urllib.request.urlopen(url)
    # contents = page.read()
    # soup = BeautifulSoup(contents)
    # print(u' 豆瓣电影TOP250:\n 序号 \t影片名\t 评分 \t评价人数 \t 链接 ')
    # for tag in soup.find_all('div', class_='item'):
        # m_order = int(tag.find('div', class_='pic').em.get_text())
        # m_name = tag.find('span',class_='title').get_text()
        # print(m_order,m_name)


# url = u'http://www.pm25.com/city/changsha.html'
# html = download(url)
# soup = BeautifulSoup(html,'html.parser')
# for a in soup.find_all('div',attrs={'class':'citydata_banner_opacity'}):
	# for b in a.find_all('div',attrs={'class':'cbol_aqi'}):
		# for c in b.find_all('a'):
			# print c.text
		

# url = u'https://www.aqistudy.cn/historydata/monthdata.php?city=上海'
# html = download(url)
# soup = BeautifulSoup(html,'html.parser')
# for a in soup.find_all('table',attrs={'class':'table table-condensed table-bordered table-striped table-hover table-responsive'}):
	# for b in a.find_all('td'):
		# if b.find_all('a'):
			# print "\r\n"
		# print b.text
			
			
url = 'http://example.webscraping.com/view/Albania-3'
html = download(url)
soup = BeautifulSoup(html,'html.parser')
for a in soup.find_all('div',attrs={'class':'span12'}):
	for b in a.find_all('tr',attrs={'id':'places_national_flag__row'}):
		print b.text
	

	




