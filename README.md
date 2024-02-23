# Goal
Analyzing topics extracted from up-to-date finance news sourced from both Yahoo and Fox.

## Scrap-data
Use [scrap_yahoo](scrap_yahoo.py) to scrap Financial News from [Yahoo Finance](https://finance.yahoo.com/).

Use [scrap_fox](scrap_fox.py) to scrap Financial News from [Fox Business](https://www.foxbusiness.com/).

### **Package used**: [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) | [requests](https://pypi.org/project/requests/)

## Topic Modeling
Use [topic_modeling](topic_modeling.py) to model topic from scraped news. 

### **Package used**: [NLTK](https://www.nltk.org/) | [Gensim](https://radimrehurek.com/gensim/) | [re](https://docs.python.org/3/library/re.html)


## Steps

Scrap current financial posts from two websites [Yahoo Finance](https://finance.yahoo.com/) and [Fox Business](https://www.foxbusiness.com/).

Scrap each article's detailed data: Title, Author, Time, and Content.

Use [LDA](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf) to generate topics each with 5 words.

## Output
[scrap_yahoo](scrap_yahoo.py): `Yahoo_Scrap.get_data()` a dataframe with the most recent financial news from Yahoo Finance.

[scrap_fox](scrap_fox.py):  `Fox_Scrap.get_data()` get a dataframe with the most recent market news from Fox Business.

[topic_modeling](topic_modeling.py):   `TopicModeling.topic_modeling()` get generated news topics.

## Package used
[pandas](https://pandas.pydata.org/) | [numpy](https://numpy.org/) | [NLTK](https://www.nltk.org/) | [Gensim](https://radimrehurek.com/gensim/) | [re](https://docs.python.org/3/library/re.html) | [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) | [requests](https://pypi.org/project/requests/)
