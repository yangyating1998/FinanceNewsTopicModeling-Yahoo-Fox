import pandas as pd
import datetime

from scrap_fox import Fox_Scrap
from scrap_yahoo import Yahoo_Scrap

from topic_modeling import TopicModeling

# Scrap data from Yahoo_finance and Fox_Business
fox = Fox_Scrap()
df_fox = fox.get_data()
yahoo = Yahoo_Scrap()
df_yahoo = yahoo.get_data()

# Store each day's news
current_date = datetime.datetime.today().strftime('%Y-%m-%d')
df_yahoo.to_csv('yahoo_{}.csv'.format(current_date))
df_fox.to_csv('fox_{}.csv'.format(current_date))

# Topic Modeling
df = pd.concat([df_yahoo, df_fox], axis=0) # replace with needed dataframe
yahoo_model = TopicModeling(df)
yahoo_model.topic_modeling()