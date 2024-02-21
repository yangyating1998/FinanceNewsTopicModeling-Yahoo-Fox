## Scrap-data-from-Yahoo-Finance
Scrap Financial News from Yahoo Finance https://finance.yahoo.com/.

Scrap Financial News from Fox Business https://www.foxbusiness.com/.

## Goal

## Steps

Scrap current financial posts from two websites Yahoo Finance and Fox Business.

Scrap each article's detailed data: Title, Author, Time, and Content.

Organize materials into two DataFrames.



## Package used
from bs4 import `BeautifulSoup`

import `requests`

import `Pandas` as pd

## Output
Scrap-Yahoo: a dataframe with the most recent financial news from Yahoo Finance.

Scrap-Fox: a dataframe with the most recent market news from Fox Business.
