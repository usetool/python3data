
#爬取qunar.com 数据

import requests
import time
from urllib import request

#出发地站点
dep_cities_url='https://touch.dujia.qunar.com/depCities.qunar'
dep_cities=requests.get(dep_cities_url)
dep_cities_dic=dep_cities.json()
dep_cities_count=0#出发地城市数量
for item in dep_cities_dic['data']:
    for dep in dep_cities_dic['data'][item]:
        # print(dep)
        dep_cities_count+=1
print("共有%u个城市"%dep_cities_count)

#根据出发地站点获取目的地
#遍历出发地城市
arrive_dict=None
for item in dep_cities_dic['data']:
    for dep in dep_cities_dic['data'][item]:
        arrive_list=[]#去重后的目的地
        print(dep+"---------")
        #格式化并对汉字进行url编码
        url='https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}&exclude=&extensionImg=255,175'.format(request.quote(dep))
        time.sleep(0.3)
        strhtml=requests.get(url)
        arrive_dict=strhtml.json()
        for arr_item in arrive_dict['data']:
            for arr_item_1 in arr_item['subModules']:
                for query in arr_item_1['items']:
                    if query['query'] not in arrive_list:
                        arrive_list.append(query['query'])
        print(arrive_list)
