#references
#https://medium.com/@mjhans83/파이썬으로-크롤링-하기-908e78ee09e0

import requests
import urllib
from bs4 import BeautifulSoup

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html
def parse_html(html):
    webtoon_list = list()
    soup = BeautifulSoup(html, 'html.parser')
    webtoon_area = soup.find("table", {"class" : "viewList"}).find_all("td", {"class": "title"})
    for webtoon_index in webtoon_area:
        info_soup = webtoon_index.find("a")
        _url = info_soup["href"]
        _text = info_soup.text.split(".")
        _title = ""
        _num = _text[0]
        if len(_text) > 1:
            _title = _text[1]
        
        webtoon_list.append((_num, _title, _url, ))
    return webtoon_list

URL = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
html = get_html(URL)
for index in parse_html(html):
    print(index)