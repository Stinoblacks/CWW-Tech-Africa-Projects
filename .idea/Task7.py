from Task5 import netflix_movie_col_subset

short_movies = netflix_movie_col_subset.loc[netflix_movie_col_subset['duration'] < 60]

print(short_movies.head(20))
short_movies.to_csv('short_movies.csv')
