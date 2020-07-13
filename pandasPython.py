import pandas as pd 
df = pd.read_csv("data/survey_results_public.csv")
# print(df)
# df.shape
# df.info()
pd.set_option('display.max_columns ' , 85)
pd.set_option('display.max_rows' , 61)
df2 = pd.read_csv("data/survey_results_schema.csv")
df.head(10)
df.tail(6)