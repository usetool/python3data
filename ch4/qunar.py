# 根据出发地和目的地获取产品列表并存入数据库
import requests
from urllib import request
import time
import pymongo

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
book_qunar = client['qunar']
sheet_qunar_zyx = book_qunar['qunar_zyx']



# 根据出发地站点获取目的地
# 遍历出发地城市
# arrive_dict=None
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'cookie': 'QN48=tc_be4c99b1337ed7cf_169d19d5757_6267; QN300=organic; QN1=ezu0pVygKEdZST0R0f+3Ag==; _RF1=120.224.7.90; _RSG=GbaTzGtwcA5rP4X0ImPol9; _RDG=283de65ea1c9b323750b8e87b399638852; _RGUID=52a6eb74-3d76-4950-9bf2-670480844675; QN205=organic; QN233=dujia_hy_destination; QN243=16',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}

#
def get_list(dep,item):
    q_product_count_url = 'https://touch.dujia.qunar.com/list?modules=list,bookingInfo,activityDetail&dep={}&query={}&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=dujia_hy_destination&date=&needNoResult=true&originalquery={}&limit=0,24&includeAD=true&qsact=search'. \
        format(request.quote(dep), request.quote(item), request.quote(item))
    p_c_json = get_json(q_product_count_url)
    if p_c_json['ret'] == True:
        print("====出发地：%s$目的地：%s start===" % (dep, item))
        # 可能没有数据
        if p_c_json['data']['limit']:
            routeCount = int(p_c_json['data']['limit']['routeCount'])  # 产品总数
            print("产品总数：(%s)" % routeCount)
            for limit in range(0, routeCount, 24):
                q_product_url = 'https://touch.dujia.qunar.com/list?modules=list,bookingInfo,activityDetail&dep={}&query={}&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=dujia_hy_destination&date=&needNoResult=true&originalquery={}&limit=0,24&includeAD=true&qsact=search'. \
                    format(request.quote(dep), request.quote(item), request.quote(item), limit)
                p_json=get_json(q_product_url)
                result = {
                    'date': time.strftime('%Y-%m-%d', time.localtime(time.time())),
                    'dep': dep,
                    'arrive': item,
                    'limit': limit,
                    'result': p_json
                }

                print("这一页数量：%d" % len(result['result']['data']['list']['results']))
                # TODO 插入数据到表中
                print("-----{}:产品end------".format(limit))
        else:
            print("没有对应的数据")
        print("====end===")
    else:
        print(p_c_json['msg'])


def get_json(url):
    strhtml=requests.get(url,headers=headers)
    time.sleep(1)
    return strhtml.json()

def get_all_data(dep):
    arrive_list = []  # 去重后的目的地
    print(dep + "---------")
    # 格式化并对汉字进行url编码
    url = 'https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}&exclude=&extensionImg=255,175'.format(
        request.quote(dep))
    arrive_dict = get_json(url)
    # 将目的地存入元组中
    for arr_item in arrive_dict['data']:
        for arr_item_1 in arr_item['subModules']:
            for query in arr_item_1['items']:
                if query['query'] not in arrive_list:
                    arrive_list.append(query['query'])
    # 迭代目的地元组
    for item in arrive_list:
        get_list(dep,item)