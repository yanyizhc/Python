# encoding:utf-8
import requests
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
# --------------------------------------------------------------------------------------------------------
# 专栏api获取地址 https://zhuanlan.zhihu.com/api/columns/zimei
#				  https://zhuanlan.zhihu.com/api/columns/专栏名
# 专栏文章api获取地址 https://zhuanlan.zhihu.com/api/columns/zimei/posts?limit=10&offset=0
#				  https://zhuanlan.zhihu.com/api/columns/专栏名/posts?limit=获取文章信息数量&offset=起始偏移
# --------------------------------------------------------------------------------------------------------

# 公共参数
# -----------------------------------------------------
default_Header = {
    'Referer': 'https://zhuanlan.zhihu.com/zimei',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;'
                  'Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    'Host': 'zhuanlan.zhihu.com'}


# 获取专栏基础内容
# -d---------------------------------------------------
def zhuanlan_jichuxingxi():
    re_session = requests.session()
    re_session.headers.update(default_Header)
    Html_zhuanlan_neirong = re_session.get('https://zhuanlan.zhihu.com/api/columns/zimei')
    Html_zhuanlan_neirong = Html_zhuanlan_neirong.json()
    print '知乎专栏名称：' + Html_zhuanlan_neirong['name'].encode('utf-8')
    print '知乎专栏关注人数：' + str(Html_zhuanlan_neirong['followersCount'])
    print '知乎专栏文章数量：' + str(Html_zhuanlan_neirong['postsCount'])
    print '# ----------------------------------------------------'


# 获取专栏文章内容
# -d---------------------------------------------------
data_zhuanlan_api = 'https://zhuanlan.zhihu.com/api/columns/'
data_zhuanlan = 'https://zhuanlan.zhihu.com'

def zhuanlan_wenzhangneirong():
    re_session = requests.session()
    re_session.headers.update(default_Header)
    wenzhangText_API = data_zhuanlan_api + 'zimei/posts?limit=5&offset='
    endFlag = True
    offset = 0
    while endFlag:
        TextContentHTML = (re_session.get(wenzhangText_API+str(offset))).json()
        for everText in TextContentHTML:
            print '1、文章标题：'+everText['title'].encode('utf-8')
            print '2、文章地址：'+data_zhuanlan+everText['url'].encode('utf-8')
            print '3、文章推送时间：'+everText['publishedTime'].encode('utf-8')
            print '4、文章评论数量：'+str(everText['commentsCount'])
            print '5、文章点赞数量：'+str(everText['likesCount'])
            print '\n'
        if(len(TextContentHTML) < 20):
            endFlag = False
        offset = offset + 20

# 测试
# -----------------------------------------------------
zhuanlan_jichuxingxi()
zhuanlan_wenzhangneirong()