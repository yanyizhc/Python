#encoding:utf-8

import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


def zhuanlan_info():
    Default_Header = {
                  'Referer': 'https://zhuanlan.zhihu.com/passer',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; '
                                'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
                  'Host': 'zhuanlan.zhihu.com'}
    _session = requests.session()
    _session.headers.update(Default_Header)
    HtmlContent = _session.get('https://zhuanlan.zhihu.com/api/columns/zimei')
    HtmlContent = HtmlContent.json()
    print '专栏名称   ：'+HtmlContent['name'].encode('utf-8')
    print '专栏关注人数：'+str(HtmlContent['followersCount'])
    print '专栏文章数量：'+str(HtmlContent['postsCount'])
    print '专栏介绍   ：'+HtmlContent['description'].encode('utf-8')
    print '专栏创建者相关信息：'
    print '1、地址：:'+HtmlContent['creator']['profileUrl'].encode('utf-8')
    print '2、个签：:'+HtmlContent['creator']['bio'].encode('utf-8')
    print '3、昵称：:'+HtmlContent['creator']['name'].encode('utf-8')
    print '4、hash：:'+HtmlContent['creator']['hash'].encode('utf-8')
    print '5、介绍：:'+HtmlContent['creator']['description'].encode('utf-8')

BASE_ZHUANLAN_API = 'https://zhuanlan.zhihu.com/api/columns/'
BASE_ZHUANLAN = 'https://zhuanlan.zhihu.com'
def zhuanlan_text():
    Default_Header = {
                  'Referer': 'https://zhuanlan.zhihu.com/passer',
                  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; '
                                'rv:39.0) Gecko/20100101 Firefox/39.0',
                  'Host': 'zhuanlan.zhihu.com'}
    #requests.session()  能够跨请求地保持某些参数比如：cookies，同一个session实例发出的所有请求都保持同一个cookies，requests模块会自动处理cookies
    _session = requests.session()
    #使用update方法，重新设定headers属性，
    _session.headers.update(Default_Header)
    TextAPI = BASE_ZHUANLAN_API+'zimei/posts?limit=20&offset='
    endFlag = True
    offset = 0
    while endFlag:
        #session对象发出get请求获取cookies
        TextContentHTML = (_session.get(TextAPI+str(offset))).json()
        for everText in TextContentHTML:
            print '文章作者相关：'
            # print '1、地址：:'+everText['author']['profileUrl'].encode('utf-8')
            # print '2、个签：:'+everText['author']['bio'].encode('utf-8')
            # print '3、昵称：:'+everText['author']['name'].encode('utf-8')
            # print '4、hash：:'+everText['author']['hash'].encode('utf-8')
            # print '5、介绍：:'+everText['author']['description'].encode('utf-8')
            print '文章标题   ：'+everText['title'].encode('utf-8')
            print '文章地址    ：'+BASE_ZHUANLAN+everText['url'].encode('utf-8')
            print '文章推送时间：'+everText['publishedTime'].encode('utf-8')
            print '文章评论数量：'+str(everText['commentsCount'])
            print '文章点赞数量：'+str(everText['likesCount'])
            # print '文章内容   ：'+everText['content'].encode('utf-8')

        if(len(TextContentHTML) < 20):
            endFlag = False
        offset = offset + 20
        print offset

# zhuanlan_info()
zhuanlan_text()