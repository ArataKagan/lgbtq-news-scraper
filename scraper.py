from bs4 import BeautifulSoup
import requests
import csv

for i in range(1,4):
    source = requests.get(f'https://www.reuters.com/news/archive/lgbt-news?view=page&page=${i}&pageSize=10').text

    soup = BeautifulSoup(source, 'lxml')
    soup = soup.find('div', class_='column1')

    # csv_file = open('crm_scrape.csv','w')
    # csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['headline','summary','video_link'])

    # for article in soup.find_all('article'):
    for article in soup.find_all('article'):
        photo = article.find('div', class_='story-photo').a.img['src']
        print(photo)

        content = article.find('div', class_='story-content')
        headline = content.a.h3.text.strip()
        print(headline)

        summary = content.p.text.strip()
        print(summary)

        time = content.time.span.text
        print(time)
        print()


# csv_writer.writerow([headline, summary, yt_link])
# csv_file.close()

