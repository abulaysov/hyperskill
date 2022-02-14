import requests
from bs4 import BeautifulSoup
import argparse


def write_file(text):
    with open(text + '.txt', 'r', encoding='utf-8') as f:
        l = f.readlines()[:-2]
        l[-1] = l[-1].strip()
    with open(text + '.txt', 'w', encoding='utf-8') as f:
        for i in l:
            f.write(i)
    with open(args.text + '.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def translate(text, from_, into):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://context.reverso.net/translation/{from_}-{into}/{text}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    words = []
    for i in soup.find_all('a', {'class': ['translation', 'trg']}):
        words.append(i.text.strip())
    v = words[1]
    assert r.status_code == 200, 'Something wrong with your internet connection'
    with open(text + '.txt', 'a', encoding='utf-8') as f:
        print(f'{into} Translations:', file=f)
        f.write(words[1] + '\n')
        print(f'\n{into} Examples:', file=f)
        x = 0
        for i in soup.find_all('div', {'class': ['src', 'trg']}):
            for j in i.findChildren('span', {'class': 'text'}):
                if x == 2:
                    f.write('\n')
                    break
                if j.text.strip() != '':
                    f.write(j.text.strip() + '\n')
                    x += 1
            if x == 2:
                break
        f.write('\n\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('from_')
    parser.add_argument('into')
    parser.add_argument('text')
    args = parser.parse_args()

    dict_language = {1: 'arabic', 2: 'german', 3: 'english', 4: 'spanish', 5: 'french', 6: 'hebrew',
        7: 'japanese', 8: 'dutch', 9: 'polish', 10: 'portuguese', 11: 'romanian', 12: 'russian', 13: 'turkish'}

    if args.from_ not in dict_language.values() and args.from_ != 'all':
        print(f"Sorry, the program doesn't support {args.from_}")
    elif args.into not in dict_language.values() and args.into != 'all':
        print(f"Sorry, the program doesn't support {args.into}")
    else:
        try:
            if args.into == 'all':
                for into_ln in dict_language.values():
                    if into_ln == args.from_:
                        continue
                    translate(args.text, args.from_, into_ln)
            else:
                translate(args.text, args.from_, args.into)
            write_file(args.text, )
        except AssertionError as err1:
            print(err1)
        except IndexError:
            print(f'Sorry, unable to find {args.text}')
