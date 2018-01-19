from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://www.youtube.com/watch?v=F4qfN5UeFvQ&list=PLFgquLnL59akp3Cc6cj1S_4fQxPhdetsO")
soup = BeautifulSoup(html, 'lxml')
lists = soup.find_all('a', {'id':'wc-endpoint'})

for list in lists:
    w = '주소 : youtube.com{1:20s}\n'.format(list['href'])
    print(w)
