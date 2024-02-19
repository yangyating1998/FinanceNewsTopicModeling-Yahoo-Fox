# Use `requests` and `BeautifulSoup` to get the text from Yahoo Finance
origin = requests.get('https://finance.yahoo.com/')
Yahoo_soup = BeautifulSoup(origin.text)

# Get all articles' links from the main body
yahoo_articles = yahoo_soup.find_all('div', id = 'Main')
links = [a['href'] for div in yahoo_articles for a in div.find_all('a')]

yahoo_data = []

# clean the links - delete not news ones
for link in pd.unique(links):
    if 'https://' not in link:
        link = 'https://finance.yahoo.com' + link
    if 'news' not in link:
        continue
        
    yahoo_article = {}

    # Get Title, Author, Posted Time, and Content (all paragraphs) from each valid link
    article_origin = requests.get(link)
    article_soup = BeautifulSoup(article_origin.text)
    yahoo_article['title'] = article_soup.find('h1').text
    yahoo_article['author'] = article_soup.find('div', class_ = 'caas-attr-item-author').text
    yahoo_article['post_time'] = article_soup.find('time').text
    
    content = []
    body = article_soup.find('div', class_='caas-body')
    paragraphs = body.find_all('p')
    for paragraph in paragraphs:
        content.append(paragraph.text.strip())

    yahoo_article['content'] = ' '.join(content).strip()
    
    yahoo_data.append(yahoo_article)

# trans json format to `pd.DataFrame` and save to `csv`
yahoo_df = pd.DataFrame(yahoo_data)
yahoo_df.to_csv('yahoo_df.csv')
