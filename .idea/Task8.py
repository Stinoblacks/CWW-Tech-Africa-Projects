from Task5 import netflix_movie_col_subset

color = []

# Use a for loop to iterate through the rows of the DataFrame
for index, row in netflix_movie_col_subset.iterrows():
    if row['genre'] == 'Children':
        color.append('red')
    elif row['genre'] == 'Documentary':
        color.append('blue')
    elif row['genre'] == 'Stand-Up':
        color.append('green')
    else:
        color.append('black')

print(color[:10])
