'''
파일명 : Crawling5-getRankPage.py
'''

import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p', class_='title')
artist_list = soup.find_all('p', class_='artist')
# print(music_list[0].text.strip())
# I AM - IVE
# print(artist_list[0].text.strip())
for idx, title in enumerate(music_list):
    print(title.text.strip(), end='-')
    print(artist_list[idx].find_all('a')[0].text.strip())


