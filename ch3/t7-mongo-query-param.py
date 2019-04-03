import pymongo

client=pymongo.MongoClient('localhost',27017)
book_weather=client['weather']
sheet_weather=book_weather['sheet_weather_3']
for item in sheet_weather.find():
    tmp=item['HeWeather6'][0]['now']['tmp']
    print(tmp)
    #将温度修改为数值型
    # sheet_weather.update_one({'_id':item['_id']},{'$set':{'HeWeather6.0.'}})