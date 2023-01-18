import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time as t


df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df.set_index(['date'], inplace=True)
# print(df)
df_clean = df.loc[(df['value'] > df['value'].quantile(0.025)) &
                  (df['value'] < df['value'].quantile(0.975))]
# print(df_clean)
fig = plt.figure(figsize=(12, 6))
plt.plot()
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
sns.lineplot(df_clean, x='date', y='value', color='red')
plt.ylabel('Page Views')
plt.xlabel('Date')
fig.savefig('line_plot.png')

df_clean.reset_index(inplace=True)
df_bar = df_clean.copy()
df_bar['Years'] = [d.strftime('%Y') for d in df_bar['date']]
df_bar['Months'] = [d.strftime('%B') for d in df_bar['date']]

avg = round(df_bar.groupby(['Years', 'Months'], as_index=False).mean())
# print(avg)
fig1 = plt.figure(figsize=(8, 8))
plt.plot()
sns.barplot(avg, x='Years', y='value', hue='Months',
            hue_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                       'November', 'December'], width=.5, palette='bright')
plt.ylabel('Average Page Views')
fig1.savefig('bar_plot.png')

df_clean.reset_index(inplace=True)
df_box = df_clean.copy()
df_box['Years'] = [d.strftime('%Y') for d in df_bar['date']]
df_box['Months'] = [d.strftime('%b') for d in df_bar['date']]
df_box['Mon'] = [d.strftime('%m') for d in df_bar['date']]
df_box.sort_values(by=['Mon', 'Months'], ascending=True, inplace=True)


fig2 = plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Year-wise Box Plot (Trend)')
sns.boxplot(df_box, x='Years', y='value')
plt.ylabel('Page Views')
plt.xlabel('Year')
plt.subplot(1, 2, 2)
plt.title('Month-wise Box Plot (Seasonality)')
sns.boxplot(df_box, x='Months', y='value', width=.5)
plt.ylabel('Page Views')
plt.xlabel('Month')
plt.show()