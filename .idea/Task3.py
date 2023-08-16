import matplotlib.pyplot as plt

from Task2 import durations_df

# plotting
durations_df.plot(kind='line', marker=0)

plt.xlabel('years')
plt.ylabel('durations')
plt.title('Netflix Movie Durations 2011-2020')
plt.show()
