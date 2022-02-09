import requests
import os
from bs4 import BeautifulSoup
import string


def correct_name(word):
    for char in string.punctuation:
        if char in word:
            word = word.replace(char, '')
    word = word.strip().replace(' ', '_')
    return word + '.txt'


n = int(input())
cont = input()
for k in range(n):
    if k == 0:
        url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020'
    else:
        url = 'https://www.nature.com' + soup.find('a', {'class': 'c-pagination__link'})['href']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    dr = f'Page_{k+1}'
    os.mkdir(dr)
    for i in soup.find_all('article'):
        if i.find('span', {'class': 'c-meta__type'}).text == cont:
            file_name = correct_name(i.a.text)
            url_news = 'https://www.nature.com' + i.a['href']
            with open(os.path.join(dr, file_name), 'w') as file:
                r = requests.get(url_news)
                text = BeautifulSoup(r.content, 'html.parser')
                text = text.find('div', {"class": "c-article-body"}).findChildren(['p', 'h2'])
                for tag in text:
                    file.write(tag.text.strip())
else:
    print('Saved all articles')
