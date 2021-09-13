from settings import URL, HUBS

import requests
from bs4 import BeautifulSoup


def habr_scrap(url=URL, hubs=HUBS):
   proxies = {
      "http": "http://9kx6mS:wqtDdw@81.177.181.133:52517/"
   }

   res = requests.get(url, proxies)
   res.raise_for_status()

   soup = BeautifulSoup(res.text, 'html.parser')

   posts = soup.find('article', class_ = 'tm-articles-list__item')

   for hub in hubs:
      if hub in posts:
         post_date = posts.find('time').attrs.get('title')
         post_title = posts.find('a', class_='tm-article-snippet__title-link').text
         post_link = posts.find('a').attrs.get('href')
         print(post_date, '-', post_title, '-', post_link)

if __name__ == '__main__':
    habr_scrap(URL, HUBS)

