import pymongo
client=pymongo.MongoClient('localhost',27017)
book_weather=client['weather']
sheet_weather=book_weather['sheet_weather_3']
#查找键为 HeWeather6.basic.admin_area值为北京的数据

for item in sheet_weather.find({'HeWeather6.basic.admin_area':'北京'}):
    print(item)