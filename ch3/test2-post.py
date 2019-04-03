import requests
import json


def get_translate_data(word=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    Form_data = {'i': word, 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict',
                 'client': 'fanyideskweb', 'salt': '15537362598011', 'sign': 'a343599ec1aff9233d3faf3cd9193231',
                 'ts': '1553736259801', 'bv': '8d165ec21fcdbdde58f225cd72fd33e4', 'doctype': 'json', 'version': '2.1',
                 'keyfrom': 'fanyi.web', 'action': 'FY_BY_REALTlME', 'typoResult': 'false'}
    response=requests.post(url,data=Form_data)
    # print(response.text)
    content=json.loads(response.text)
    # print(content)
    print(content['translateResult'][0][0]['tgt'])

if __name__=='__main__':
    get_translate_data('我爱数据')
