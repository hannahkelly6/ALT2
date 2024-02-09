import matplotlib.pyplot as plt

# Data to plot
labels = ['Google Chrome', 'Snapchat', 'Instagram', 'Tiktok', 'Youtube']
sizes = [9.1, 27.3, 18.2, 27.3, 18.2]  # Percentages
colors = ['orange', 'green', 'yellow', 'red', 'blue']
explode = (0, 0.1, 0, 0.1, 0)  # explode 2nd & 4th slice (i.e. 'Snapchat & Tiktok')

# Plot
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Most used app')

plt.show()
