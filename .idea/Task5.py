from Task4 import netflix_df

netflix_df_movies_only = netflix_df.loc[netflix_df['type'].isin(['Movie'])]


netflix_movie_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

print(netflix_movie_col_subset.head(5))
