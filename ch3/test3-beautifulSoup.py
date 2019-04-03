from bs4 import BeautifulSoup
import requests
import re

url='https://www.cnblogs.com/'
selector='#post_list > div > div.post_item_body > h3 > a'
response=requests.get(url=url)
soup=BeautifulSoup(response.text,'lxml')
data=soup.select(selector)
#清洗和组织数据
print(data[0])
for item in data:
    result={
        'title':item.get_text(),
        'link':item.get('href'),
        'id':re.findall('(?<=/p/).*?(?=.html)',item.get('href'))
    }
    print(result)