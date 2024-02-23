import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

class Fox_Scrap: # Check naming convention
    def __init__(self, url='https://www.foxbusiness.com/'):
        self.url = url

    # Request original data from Fox_Business url
    def get_data(self):
        origin = requests.get(self.url)
        fox_soup = BeautifulSoup(origin.text, features='html.parser')
        fox_articles = fox_soup.find_all('main')
        links = [a['href'] for div in fox_articles for a in div.find_all('a')]
        print(links)
        return self.clean_data(links)

    # Get Title, Author, Posted Time, and Content (all paragraphs) from each valid link
    def clean_data(self, links):
        fox_data = []

        for link in np.unique(links):
            if ('category' in link) or ('video' in link) or ('foxnews' in link):
                continue
            print(link) # check to see whether there are some new problems of news scraping
            fox_article = {}

            article_origin = requests.get(link)
            article_soup = BeautifulSoup(article_origin.text, features='html.parser')
            fox_article['title'] = article_soup.find('h1').text
            fox_article['author'] = article_soup.find('div', class_='author-byline').text
            fox_article['post_time'] = article_soup.find('time').text

            content = []
            body = article_soup.find('div', class_='article-body')
            paragraphs = body.find_all('p')

            for paragraph in paragraphs:
                content.append(paragraph.text.strip())

            fox_article['content'] = ' '.join(content).strip()

            fox_data.append(fox_article)

        fox_df = pd.DataFrame(fox_data)
        return fox_df