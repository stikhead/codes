# if numpy is underlying c array then pandas is the database built on top of it.
# it is desgined to take messy, tabular data (like a csv file or an sql table)
# and load it directly into memory as an object called dataframe


import pandas as pd

# load a csv into memory as a dataframe
df = pd.read_csv(r"F:\codes\codes\python\pandas\01_prac\raw_data.csv")


# look at the first 5 rows to make sure it loaded right
print(df.head())

# grab a specific column and turn it into a python list
text_list = df['hindi_text'].tolist()

# drops any rows where the data is missing or corrupted
clean_df = df.dropna()