import requests

url='https://www.cnblogs.com'
strhtml=requests.get(url)
print(strhtml.text)