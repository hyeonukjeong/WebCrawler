# coding:utf-8
from bs4 import BeautifulSoup
from urllib.request import urlopen
fout = open('image.html', 'w')

html = urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, 'lxml')
fout.write('<!DOCTYPE>\n<HTML>')

image = soup.find_all('img')
for m in image:
    print(m.get('src'))
    w = '<img src = {0:20s}>\n'.format(m.get('src'))
    fout.write(w)

fout.write('</HTML>')
fout.close()
