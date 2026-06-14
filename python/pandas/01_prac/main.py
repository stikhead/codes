import numpy as np
import pandas as pd
import time
df = pd.read_csv(r"F:\codes\codes\python\pandas\01_prac\raw_data.csv")

print(df.head(7))

clean_dataframe = df.dropna()

print(clean_dataframe.head())

list_time = time.time()
# hindi_list = [line for line in clean_dataframe['hindi_sentence']]
# english_list.insert(2, "hey")
# print(len(english_list))
# print(hindi_list)
english_list = [line for line in clean_dataframe['english_sentence']]
print(english_list)
print(f"{time.time() - list_time} seconds taken")

numpy_time = time.time()
panda_list = clean_dataframe['english_sentence'].tolist()
eng_arr = np.array(panda_list)
print(eng_arr.shape)
print(panda_list)
# hindi_arr = np.array(hindi_list)
# print(hindi_arr)
print(f"{time.time() - numpy_time} seconds taken")

