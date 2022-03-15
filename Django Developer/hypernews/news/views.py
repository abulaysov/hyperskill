from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.conf import settings
from datetime import datetime
from random import random
import re


def index(request):
    return redirect('news/')


def mainpage(request):
    with open('hypernews/news.json', 'r') as data:
        json_data = json.load(data)
    new_l = []
    if request.GET.get('q'):
        q = request.GET.get('q')
        for i in json_data:
            if q in i['title']:
                new_l.append(i)
    else:
        new_l = json_data
    l = sorted(new_l, key=lambda x: x['created'], reverse=True)
    news_d = {}
    for i in l:
        news_d.setdefault(i['created'][:10], [])
        d = {'title': i['title'], 'link': i['link']}
        if len(news_d[i['created'][:10]]) == 0:
            d['created'] = i['created'][:10]
        news_d[i['created'][:10]].append(d)
    news_d = {'date': news_d}

    return render(request, 'news/mainpage.html', {'data': news_d})


def news(request, link):
    with open('hypernews/news.json', 'r') as data:
        json_data = json.load(data)
        for i in json_data:
            if link == i['link']:
                break
        return render(request, 'news/index.html', context=i)


def create(request):
    if request.method == 'POST':
        with open('hypernews/news.json', 'r') as data:
            json_data = json.load(data)
            new_news = {"created": str(datetime.now())[:19],
                        "text": request.POST.get("text"),
                        "title": request.POST.get("title"),
                        "link": str(random())[2:]}
            json_data.append(new_news)
        with open('hypernews/news.json', 'w') as data:
            json_data = json.dumps(json_data)
            data.write(str(json_data))
        return redirect('/news')
    return render(request, 'news/articles.html')