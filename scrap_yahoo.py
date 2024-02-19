import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

class Yahoo_Scrap: # Check naming convention
    def __init__(self, url='https://finance.yahoo.com/'):
        self.url = url

    # Request original data from Yahoo_Finance url
    def get_data(self):
        origin = requests.get(self.url)
        yahoo_soup = BeautifulSoup(origin.text, features='html.parser')
        yahoo_articles = yahoo_soup.find_all('div', id = 'Main')
        links = [a['href'] for div in yahoo_articles for a in div.find_all('a')]
        return self.clean_data(links)

    # Get Title, Author, Posted Time, and Content (all paragraphs) from each valid link
    def clean_data(self, links):
        yahoo_data = []

        # clean the links - delete not news ones
        for link in np.unique(links):
            if 'https://' not in link:
                link = self.url + link
            if 'news' not in link:
                continue

            yahoo_article = {}

            article_origin = requests.get(link)
            article_soup = BeautifulSoup(article_origin.text, features='html.parser')
            yahoo_article['title'] = article_soup.find('h1').text
            yahoo_article['author'] = article_soup.find('div', class_='caas-attr-item-author').text
            yahoo_article['post_time'] = article_soup.find('time').text

            content = []
            body = article_soup.find('div', class_='caas-body')
            paragraphs = body.find_all('p')
            for paragraph in paragraphs:
                content.append(paragraph.text.strip())
            yahoo_article['content'] = ' '.join(content).strip()

            yahoo_data.append(yahoo_article)

        yahoo_df = pd.DataFrame(yahoo_data)
        return yahoo_df
