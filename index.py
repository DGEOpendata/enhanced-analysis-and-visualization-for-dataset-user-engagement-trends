python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Daily_Views_and_Downloads_March_2026.csv')

# Convert the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Calculate basic metrics
data['Day'] = data['Date'].dt.day_name()
avg_views = data['Views'].mean()
avg_downloads = data['Downloads'].mean()

print(f'Average Daily Views: {avg_views}')
print(f'Average Daily Downloads: {avg_downloads}')

# Plot views and downloads over time
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Views'], label='Views', marker='o')
plt.plot(data['Date'], data['Downloads'], label='Downloads', marker='o')
plt.title('Daily Views and Downloads (March 2026)')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.grid()
plt.show()

# Heatmap for views and downloads by day of the week
heatmap_data = data.groupby('Day').mean()[['Views', 'Downloads']]
heatmap_data = heatmap_data.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

plt.figure(figsize=(8, 5))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".1f")
plt.title('Average Views and Downloads by Day of the Week')
plt.show()

# Correlation between views and downloads
correlation = data[['Views', 'Downloads']].corr().iloc[0,1]
print(f'Correlation between Views and Downloads: {correlation}')

sns.scatterplot(x='Views', y='Downloads', data=data)
plt.title('Correlation Between Views and Downloads')
plt.xlabel('Views')
plt.ylabel('Downloads')
plt.grid()
plt.show()
