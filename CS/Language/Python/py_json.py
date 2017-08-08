# 教程网址：https://www.youtube.com/channel/UCAx4nmhI7S1RcPiaG-Uw0tg
# json module of python tutorial: from lec 32 to 35
# lec 32
# matrials:
# maps API of google: https://developers.google.com/maps/documentation/geocoding/start
# a URI to request some map info : http://maps.googleapis.com/maps/api/geocode/json?address=nanjing

# json.dumps('类就是文档') 可以把括号中文档转换成json 标准格式
import json
import urllib.parse
import requests

stuff = {
    "long_name": "南京市",
    "short_name": "南京市",
    "types": [
        "locality",
        "political"
    ]
}

json_stuff = json.dumps(stuff)

# lec 33
main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

# lec 35
# 循环输入直到输入地址为 'quit' or 'q' 退出循环
while True:
    address = input('Address: ')

    if address == 'quit' or address == 'q':
        break
    #  url 中是不允许出现【空格】的，因为空格会被转换成unicode 还是 ascii 码
    #  eg. http://maps.googleapis.com/maps/api/geocode/json=lhr
    #  如果输入空格会变成‘％20’：
    #  http://maps.googleapis.com/maps/api/geocode/json=l%20hr
    #  如果非要输入空格，需要使用‘＋’号：
    #  http://maps.googleapis.com/maps/api/geocode/json=l+hr
    #  这里使用 urllib.parse.urlencode() 就可以不用担心这种类似的转换，
    #  这一转换工作（eg, whiteSpace -> '+'）自动进行。
    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)

    # 从指定 URL 中获取网页的 response,并将其转换成 python 的 json 格式
    # python 的 json 格式是：
    #  1. 外层 dict
    #  2. dict.key   is string
    #  3. dict.value is a list of dict

    json_data = requests.get(url).json()

    # compare with another tutorial code : py_json_earthquake.py
    # there is another code for getting the response of
    # request to certain URL.
    # But from this stackoverflow's answer, I think requests is the better one
    # ref to : https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module
    # print(json_data)

    # lec 34

    json_status = json_data['status']
    print('API Status: ' + json_status)

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print(formatted_address)
