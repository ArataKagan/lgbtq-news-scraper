from bs4 import BeautifulSoup
from pprint import pprint
from random import randint
from dotenv import dotenv_values
import os
import requests
import csv
import pymongo


MONGO_PW = dotenv_values(".env")['MONGO_PW']
print(MONGO_PW)

client = pymongo.MongoClient(
    f"mongodb+srv://admin:{MONGO_PW}@lgbtq-news.acrch.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
print(db)

# print(os.environ.get('USER'))


for i in range(1, 4):
    source = requests.get(
        f'https://www.reuters.com/news/archive/lgbt-news?view=page&page=${i}&pageSize=10').text

    soup = BeautifulSoup(source, 'lxml')
    soup = soup.find('div', class_='column1')

    for article in soup.find_all('article'):
        photo = article.find('div', class_='story-photo').a.img['src']
        # print(photo)

        content = article.find('div', class_='story-content')
        url = 'https://www.reuters.com' + content.a['href']
        # print(url)
        headline = content.a.h3.text.strip()
        # print(headline)
        summary = content.p.text.strip()
        # print(summary)

        time = content.time.span.text
        # print(time)

        article = {
            "photo": photo,
            "url": url,
            "headline": headline,
            "summary": summary,
            "time": time
        }

        print(article)

        db.news.update_one(
            {"headline": headline},
            {"$setOnInsert": article},
            upsert=True
        )

        print()


# source = requests.get('https://www.lgbtqnation.com/news/').text
# soup = BeautifulSoup(source, 'lxml')
# soup = soup.find('div', class_='main-col')

# for item in soup.find_all('li', class_='list-item'):

#     photo = item.img['src']
#     print(photo)
#     headline = item.h3.a.text
#     print(headline)
#     url_link = item.h3.a['href']
#     print(url_link)

#     excerpt = item.find('div', class_='excerpt')
#     summary = excerpt.p.text
#     print(summary)

#     time = item.find('div', class_='post-meta')
#     time = time.time.text
#     print(time)

#     print()
