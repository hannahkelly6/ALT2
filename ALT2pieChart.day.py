import matplotlib.pyplot as plt

# Data to plot
labels = ['Friday', 'Wednesday', 'Saturday', 'Monday']
sizes = [9.1, 9.1, 18.2, 63.6]  # Percentages
colors = ['green', 'yellow', 'red', 'blue']
explode = (0, 0, 0, 0.1)  # explode 4th slice (i.e. 'Monday')

# Plot
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Most used day')

plt.show()
