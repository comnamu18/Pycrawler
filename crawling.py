"""
Dataset Source = KBReport.com
Just for private study
"""
import locale
import requests
import urllib
from bs4 import BeautifulSoup

outfielder = ("우익수", "좌익수", "중견수", "외야수")
catcher = "포수"
shortstop = "유격수"
left = "좌타"
right = "우타"
both = "양타"

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html
def hand_change(hand):
    ret = ""
    if left in hand:
        ret = "왼손"
    elif right in hand:
        ret = "오른손"
    elif both in hand:
        ret = "양손"
    return ret
def position_change(position):
    ret = ""
    if catcher in position:
        ret = "포수"
    elif shortstop in position:
        ret = "유격수"
    else:
        flag = 0
        for index in outfielder:
            if index in position:
                ret = "외야수"
                flag = 1
        if flag == 0:
            ret = "내야수"
    return ret
"""
Dollar change is not ready yet
Since $ can't detected
"""
def money_change(payment, money_type):
    money = ""
    if payment is not None:
        if "￦" in payment:
            payment = payment.split("￦")[1]
            payment = ''.join(a for a in payment if a not in ',')
            money = payment[:-4]
        else:
            money = payment[payment.find("$") + 1 : -5]
    return money
def parse_html(html):
    player_info_ret = list()
    soup = BeautifulSoup(html, 'html.parser')
    player_info_area = soup.find("div", {"class" : "player-info-box"})
    name = player_info_area.find("span", 
        {"class": "player-info-title"}).text.strip()
    age = player_info_area.find("span", {"class" : 
        "player-info-1"}).text.strip()
    
    hand = player_info_area.find("span", {"class" : 
        "player-info-2"}).text.strip()
    hand = hand_change(hand)
    
    position = player_info_area.find("span", {"class" : 
        "player-info-4"}).text.strip()
    position = position_change(position)
    
    contract = player_info_area.find("span", {"class" : 
        "player-info-7"}).text.strip()
    contract = money_change(contract, "계약금")
    
    payment = player_info_area.find("span", {"class" : 
        "player-info-8"}).text.strip()
    payment = money_change(payment, "연봉")    
    
    player_info_ret.append((name, age, hand, position, contract, payment))
    return player_info_ret

URL = "http://www.kbreport.com/player/detail/317"
html = get_html(URL)
for index in parse_html(html):
    print(index)