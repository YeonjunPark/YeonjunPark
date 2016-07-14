import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from webtoon.models import Episode

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def main():
    for page in range(1, 10000):
        params = {
            'titleId': 641253,
            'page': page,
        }
        page_url = 'http://comic.naver.com/webtoon/list.nhn'
        html = requests.get(page_url, params=params).text
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.select('.viewList .title a'):
            title = a_tag.text
            link = urljoin(page_url, a_tag['href'])
            print(title, link)
            try:
                Episode.objects.get(url=link)
                print('End')
                return
            except Episode.DoesNotExist:
                Episode.objects.create(title=title, url=link)


if __name__ == '__main__':
    main()