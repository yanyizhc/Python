import re
import urllib
import urlparse
from bs4 import BeautifulSoup

author = 'Meditator_hkx'

def data_collect(url, soup):
    data_want = {}
    data_want['url'] = url
    title_node = soup.find('dd', attrs = {'class' : 'lemmaWgt-lemmaTitle-title'}).find('h1')
    data_want['title'] = title_node.getText()

    # <div class="lemma-summary" label-module="lemmaSummary">
    sum_node = soup.find('div', attrs = {'class' : 'lemma-summary'})
    data_want['summary'] = sum_node.getText()

    return data_want

data_list = list()

urls_new = list() #Store urls that have not been crawed
urls_old = list() #Store urls that have been crawed

url = raw_input('Enter-')
if len(url) < 1 : url = 'http://baike.baidu.com/item/Python'

urls_new.append(url) # Add initial url to url_new

count = 1
while len(urls_new) > 0:
    try:

        url = urls_new.pop()
        urls_old.append(url)
        print ('Crawing %d url:%s' %(count, url))

        ##Download and Prettify Using BeautifulSoup
        response = urllib.urlopen(url)
        count = count + 1

        #print 'code:', response.getcode()
        data = response.read()
        soup = BeautifulSoup(data, "html.parser")

        my_data = data_collect(url, soup)
        data_list.append(my_data)


    #    print('url:%s\ntitle:%s\nsummary:%s\n' %(data_want['url'], data_want['title'], data_want['summary']))

        ##Find urls and add them to urls_new
        links = soup.findAll('a', href = re.compile(r'/item/.*'))
        for link in links:
            incomplete_url = link['href']
            complete_url = urlparse.urljoin(url, incomplete_url)
            if complete_url not in urls_new and complete_url not in urls_old:
                urls_new.append(complete_url)

    except:
        print 'Craw failed!'

    if count > 20 :
        break


##Store data in file
fhand = open('baike.txt', 'w')
for dic in data_list:
    line = 'url:%s\ntitle:%s\nsummary:%s\n' %(dic['url'].encode('utf-8'), dic['title'].encode('utf-8'), dic['summary'].encode('utf-8'))
    fhand.write(line)
    fhand.write('\n')

fhand.close()