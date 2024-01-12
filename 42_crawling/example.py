__author__ = 'teacher'

# BeautifulSoup : HTML Parsing Library
# install : pip install beautifulsoup4
# http://www.crummy.com/software/BeautifulSoup/

import urllib.request
from bs4 import BeautifulSoup

def example():
    html = '<body><div class="article"><span><a href=http://naver.com>naver.com</a></span></div></body>'
    soup = BeautifulSoup(html, "html.parser")
    print(soup.prettify())

    # tag로 추출하기
    article = soup('a')     # a tag 추출
    print(article)

    # tag와 속성으로 추출하기
    article = soup('div', {'class':'article',})    # div내의 article class 추출
    print(article)

example()

# <li>
# <a href="/webtoon/list.nhn?titleId=642604&weekday=sat" onclick="clickcr(this,'thm*s.tit','','22',event)" class="title" title="화이트멜로우">화이트멜로우</a>
# </li>
# <a class="title" href="/webtoon/list.nhn?titleId=602910&amp;weekday=mon" onclick="clickcr(this,'thm*m.tit','','6',event)" title="윈드브레이커">윈드브레이커</a>

def webtoon():
    html = urllib.request.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
    soup = BeautifulSoup(html, "html.parser")
    cartoons = soup.find_all("a", attrs={'class':'title'})

    for tag in cartoons:
        # print(type(tag), tag)
        print("요일 : {}, title : {}, link : {}".format(tag['href'][-3:], tag.text, tag['href']))
        # tag['title']로 해도 됨

webtoon()


import json
from pprint import pprint

def melon():
    req = urllib.request.Request("http://apis.skplanetx.com/melon/charts/realtime?version=1&page=1&count=10")
    req.add_header("appKey", "dabbe642-79d5-3f6a-a0cc-e9377765b96f")

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    # json string -> dictionary로 변환
    data = json.loads(html)
    pprint(data)

melon()


def geocoding():

    address = input('Enter location: ')
    url = 'http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=' + address
    print('Retrieving', url)

    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

    html = response.read().decode('utf-8')
    print(html)

    data = json.loads(html)
    pprint(data)

    # if 'status' not in data or data['status'] != 'OK':
    #     print('==== Failure To Retrieve ====')
    #     print(data)

    lat = data["results"][0]["geometry"]["location"]["lat"]
    lng = data["results"][0]["geometry"]["location"]["lng"]
    print('lat:',lat,'lng:',lng)

    location = data['results'][0]['formatted_address']
    print(location)

geocoding()