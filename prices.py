import requests
import json
import re
from bs4 import BeautifulSoup


def gamePrice(game_id):
    r = requests.get('http://store.steampowered.com/api/appdetails?appids='+game_id+'&cc=ru&l=ru').content
    a = json.loads(r)
    b = a[game_id]['data']['price_overview']['final_formatted']
    return(b[:-5])

def badgePrice(game_id):
    page = requests.get('https://steamcommunity.com/market/search?q=&category_753_Game%5B%5D=tag_app_'+game_id+'&category_753_cardborder%5B%5D=tag_cardborder_0&appid=753').content
    soup = BeautifulSoup(page, 'lxml')
    search = soup.find_all("span", {"data-currency" : True})
    total = re.findall("\d+\.\d+", str(search))
    total = sum(map(float,total))
    return(total)