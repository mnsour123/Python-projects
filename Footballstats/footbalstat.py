import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://www.football-data.co.uk/mmz4281/2324/E0.csv"
df = pd.read_csv(url)

print(df.shape)
print(df.head())


df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)


df['TotalGoals'] = df['FTHG'] + df['FTAG']


home = df.groupby('HomeTeam')['FTHG'].sum()
away = df.groupby('AwayTeam')['FTAG'].sum()
goals_scored = (home.add(away, fill_value=0)).sort_values(ascending=False)
print(goals_scored)


plt.figure(figsize=(10, 6))
goals_scored.plot(kind='bar')
plt.title('Total Goals Scored by Team')
plt.ylabel('Goals')
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 5))
sns.countplot(x='FTR', data=df, order=['H', 'D', 'A'])
plt.title('Match Result Distribution (Home/Draw/Away)')
plt.show()


plt.figure(figsize=(10, 4))
df.set_index('Date')['TotalGoals'].resample('W').mean().plot()
plt.title('Average Goals per Match Over Time')
plt.ylabel('Avg Goals')
plt.show()
