from scrap_fox import Fox_Scrap
from scrap_yahoo import Yahoo_Scrap

# Scrap data from Yahoo_finance and Fox_Business
fox = Fox_Scrap()
df_fox = fox.get_data()
yahoo = Yahoo_Scrap()
df_yahoo = yahoo.get_data()

# What to be expected next: topic modeling and comparison