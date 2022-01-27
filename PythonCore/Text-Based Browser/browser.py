import argparse
import os
from collections import deque
import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()


def file_opening(path):
    if path == 'dir':
        if os.access(path, os.F_OK):
            return False
        else:
            os.mkdir(path)
            return path
    else:
        if not os.access(path, os.F_OK):
            os.mkdir(path)
        return path


def add_file(url_address, path_file):
    if os.access(path, os.F_OK):
        global stack
        try:
            result = ''
            with open(path_file, 'a', encoding='utf-8') as file:
                r = requests.get(url_address)
                tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
                soup = BeautifulSoup(r.content, 'html.parser').find_all(tags)
                for i in soup:
                    if i.name == 'a':
                        result += Fore.BLUE + i.text + '\n'
                    else:
                        result += i.text + '\n'
                print(result, file=file)
                print(result)
                stack.append(result)
        except requests.exceptions.ConnectionError:
            print('Incorrect URL')


def read_file(file):
    if file in os.listdir():
        with open(file, 'r') as f:
            print(f.read())
    else:
        print('Error: File not found.')


def back():
    global stack
    stack.pop()
    print(stack.pop())


url = input()
stack = deque()
path = file_opening(args.path)
while url != 'exit':
    # if re.match(r'[A-Za-z\d]+$', url):
    #     read_file(url)
    if url == 'back':
        back()
    elif not url.startswith('https://'):
        url = 'https://' + url
    name_file = re.search(r'/[\w]+', url).group()[1:]
    path_name = os.path.join(path, name_file)
    add_file(url, path_name)
    url = input()