from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, 'lxml')
titles = soup.find_all('a', 'title')

print('html', html)

print('soup', soup)

print('titles', titles)
