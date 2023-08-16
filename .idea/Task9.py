from Task5 import netflix_movie_col_subset
from Task8 import color
import matplotlib.pyplot as plt

netflix_movie_col_subset.plot.scatter(x='release_year', y='duration', c=color, alpha=0.8)
plt.xlabel('Release year')
plt.xlabel('Duration(mins')
plt.title('Movie duration by year of release')

plt.show()
