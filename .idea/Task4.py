import pandas as pd

path = r'C:\Users\hp\Downloads\netflix_data.csv'

netflix_df = pd.read_csv(path)

print(netflix_df.head(5))
