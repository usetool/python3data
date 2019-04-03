import requests
import time

#中国城市列表
china_city_list_url='https://cdn.heweather.com/china-city-list.csv'
response=requests.get(china_city_list_url);
data=response.text
rowData=data.split("\r\n")

for i in range(2):
    rowData.remove(rowData[0])

for i in range(10):
    city_code =rowData[i][0:11]
    print(city_code)
    weather_url='https://free-api.heweather.net/s6/weather/now?location='+city_code+'&key=f68bbf07aa864bd2b7be7b67817a7a12'
    response=requests.get(weather_url)
    dic=response.json()
    print(dic)
    time.sleep(1)

