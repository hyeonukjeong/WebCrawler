from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, 'lxml')
titles = soup.find_all('a', 'title')

for title in titles:
    w = '제목 : {0:20s}\n링크 : comic.naver.com{1:20s}\n'.format(title['title'], title['href'])
    print(w)
