import requests
import json


def get_translate_data(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    Form_data = {'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict',
                 'client': 'fanyideskweb', 'salt': '15537362598011', 'sign': 'a343599ec1aff9233d3faf3cd9193231',
                 'ts': '1553736259801', 'bv': '8d165ec21fcdbdde58f225cd72fd33e4', 'doctype': 'json', 'version': '2.1',
                 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME', 'typoResult': 'false'}
    headers={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Connection': 'keep-alive',
'Content-Length': '258',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': '_ga=GA1.2.1160554542.1543811147; OUTFOX_SEARCH_USER_ID_NCOO=926706804.4047585; OUTFOX_SEARCH_USER_ID="1721833325@10.168.11.15"; _ntes_nnid=90b605c27e628eb77fcf59b439be02ce,1544398694405; JSESSIONID=aaaoYK-NoEKDjbmPy5bNw; ___rl__test__cookies=1553739520386',
'Host': 'fanyi.youdao.com',
'Origin': 'http://fanyi.youdao.com',
'Referer': 'http://fanyi.youdao.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}

    response=requests.post(url,data=Form_data,headers=headers)
    print(response.text)
    content=json.loads(response.text)
    # print(content)
    print(content['translateResult'][0][0]['tgt'])

if __name__=='__main__':
    get_translate_data('我爱数据')
