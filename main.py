from settings import URL, HUBS, SITE

import re
import requests
from bs4 import BeautifulSoup


def habr_scrap(url=URL, hubs=HUBS):
   res = requests.get(url)
   res.raise_for_status()

   soup = BeautifulSoup(res.text, 'html.parser')
   posts = soup.find_all('article')

   for post in posts:
      post_title = post.find('h2')
      post_link = post_title.find('a').attrs.get('href')
      post_link = SITE + post_link

      res = requests.get(post_link)
      res.raise_for_status()

      soup = BeautifulSoup(res.text, 'html.parser')
      full_post = soup.find('div', class_='tm-page-article__body')

      post_date = full_post.find('time').attrs.get('title')

      post_title_text = full_post.find('h1', class_='tm-article-snippet__title_h1').text.strip().lower()
      post_title_text = re.split('\W+', post_title_text)

      post_hub = full_post.find('div', class_='tm-article-snippet__hubs').text.strip().lower()
      post_hub = re.split('\W+', post_hub)

      post_preview = full_post.find('div', class_='tm-article-body').text.strip().lower()
      post_preview = re.split('\W+', post_preview)

      full_preview = post_title_text + post_hub + post_preview


      for hub in hubs:
         if hub in full_preview:
            print(post_date, '-', post_title.text, '-', post_link)


if __name__ == '__main__':
    habr_scrap(URL, HUBS)

