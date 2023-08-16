import pandas as pd

from Task1 import movie_dict

durations_df = pd.DataFrame({'duration': movie_dict.values()}, index=movie_dict.keys())

print(durations_df)
