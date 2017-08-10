#encoding:utf-8
#爬取网易云 ID为550994494 歌单
import requests
import urllib
from tqdm import tqdm
from time import sleep
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
#通过使用requests.get方法获取网址

def wangyiyun_music():
	print u'请输入网易云歌单id:'
	music_id_i = input(u'>')
	music_id = str(music_id_i)
	url = 'http://music.163.com/api/playlist/detail?id=' + music_id
	r_url = requests.get(url)
	# 使用.json() 方法,并且解析网址result中tracks 属性
	r_json = r_url.json()['result']['tracks']
	music_Count = r_url.json()['result']['trackCount']
	print url
	for i in range(music_Count):
		try:
			music_name = r_json[i]['name'] + '-' + r_json[i]['artists'][0]['name'] + '.mp3'
			music_link = r_json[i]['mp3Url']
			if (music_link is ''):
				print u'地址是空的跳过'
				break
			else:
				music_out = u'开始下载: ' + music_name
				print music_out
				print music_link
				# urlretrieve函数,并且传递三个参数,(规范的URL路径,本地存储路径,任何定义的行为)
				# 并且urllib2 当做 urllib 扩展，但是urlretrieve 等一系列功能并没有加入到URLlib2中。
				for i in tqdm(range(5)):
					urllib.urlretrieve(music_link, 'wangyiyun_music\\' + music_name)
				sleep(0.1)
				print u'下载完成'
		except urllib.error.HTTPError as e:
			print u'HTTPError 错误' + music_link
			pass

	print u'总歌曲数: %s ' % music_Count


wangyiyun_music()
