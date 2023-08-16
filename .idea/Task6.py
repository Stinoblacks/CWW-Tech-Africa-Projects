from Task5 import netflix_movie_col_subset

netflix_movie_col_subset.plot.scatter(x='release_year', y='duration')
plt.xlabel('release_year')
plt.ylabel('duration')
plt.title('Movie Duration By Year of Release')

plt.show()
