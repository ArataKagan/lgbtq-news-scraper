from bs4 import BeautifulSoup
import requests
import csv

# for i in range(1,4):
#     source = requests.get(f'https://www.reuters.com/news/archive/lgbt-news?view=page&page=${i}&pageSize=10').text

#     soup = BeautifulSoup(source, 'lxml')
#     soup = soup.find('div', class_='column1')

    # csv_file = open('crm_scrape.csv','w')
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['headline','summary','video_link'])

    # for article in soup.find_all('article'):
    # for article in soup.find_all('article'):
    #     photo = article.find('div', class_='story-photo').a.img['src']
    #     print(photo)

    #     content = article.find('div', class_='story-content')
    #     url = 'https://www.reuters.com' + content.a['href']
    #     print(url)
    #     headline = content.a.h3.text.strip()
    #     print(headline)
    #     summary = content.p.text.strip()
    #     print(summary)

    #     time = content.time.span.text
    #     print(time)
    #     print()


# csv_writer.writerow([headline, summary, yt_link])
# csv_file.close()
source = requests.get('https://www.lgbtqnation.com/news/').text
soup = BeautifulSoup(source, 'lxml')
soup = soup.find('div', class_='main-col')

for item in soup.find_all('li', class_='list-item'):

    photo = item.img['src']
    print(photo)
    headline = item.h3.a.text
    print(headline)
    url_link = item.h3.a['href']
    print(url_link)

    excerpt = item.find('div', class_='excerpt')
    summary = excerpt.p.text
    print(summary)

    time = item.find('div', class_='post-meta')
    time = time.time.text
    print(time)

    print()

