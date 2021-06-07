# -*- coding: utf-8 -*-
"""
Spyder Editor

Andrew Lujan
MSDS 670- Data Visualization
Week 5- Matplotlib
John Koenig
June 5th, 2021

"""



#%%

## Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

project_dir = 'C:\\Users\\Andrew\\Desktop\\Data Science Tools\\Regis\\MSDS 670 - Data Visualization\\Week 5- Matplotlib I\Assignments'

#%% 
# Data Source:Kaggle Video Game Sales
# https://www.kaggle.com/gregorut/videogamesales


df_videogame = pd.read_csv('vgsales.csv')

print(df_videogame.head())

#%%

columns = list(df_videogame.columns)

print(columns)

platform_counts = df_videogame['Platform'].value_counts(ascending= True)

print(platform_counts)

platform = pd.Series(list(platform_counts.index))

platform_counts.index = range(len(platform_counts))

#%%
# horizontal bar chart

fig, ax = plt.subplots(figsize=(6,8))

ax.barh(platform, platform_counts)

ax.set_title('Count of Games Sold by Platform')

ax.set_xlabel('Games Sold')

ax.set_ylabel('Platform')

ax.set_yticklabels(platform, fontsize = 8)

plt.tight_layout()

plot1_filename = 'Videogame_Bar.png'

fig.savefig(project_dir + plot1_filename)

#%% 

# histogram

genre_group = df_videogame.groupby(['Year','Genre']).count()

year = 2010

genre_group = genre_group.loc[year].Name

fig, ax = plt.subplots(figsize=(6,8))

ax.bar(genre_group.index, genre_group.values, color = 'green')

ax.set_title('Games Sold by Genre in ' + str(year))

ax.set_xlabel('Genre')

ax.set_ylabel('Games Sold')

plt.xticks(rotation = 90)

plt.tight_layout()

plot2_filename = 'Videogame_Histogram.png'

fig.savefig(project_dir + plot2_filename)

#%%

# Line plot of Games sold over the years

sales_genre = df_videogame.groupby(['Genre', 'Year']).Global_Sales.count()

action = sales_genre.loc['Action']

sports = sales_genre.loc['Sports']

strategy = sales_genre.loc['Strategy']

fig, ax = plt.subplots(figsize=(6,8))

ax.plot(action.index, action.values, label = 'Action')

ax.plot(sports.index, sports.values, label = 'Sports')

ax.plot(strategy.index, strategy.values, label = 'Strategy')

ax.set_xlabel('Year')

ax.set_ylabel('Games Sold')

ax.set_title('Sales for Action, Sports, Strategy genres')

ax.legend()

plot3_filename = 'Videogames_LinePlot.png'

fig.savefig(project_dir + plot3_filename)


#%%

## Seaborn Visualization

# Heatmap for Correlation

import seaborn as sns

fig, ax = plt.subplots(figsize=(6,8))

sns.heatmap(df_videogame.corr(), cmap = "Blues", annot=True, linewidth=3)

plot4_filename = 'Videogame_heatmap.png'

fig.savefig(project_dir + plot4_filename)

#%%


# Seaborn Bar Chart

sales_by_platform = df_videogame.groupby(by=['Platform'])['Global_Sales'].sum()
sales_by_platform = sales_price_platform.reset_index()
sales_by_platform = sales_price_platform.sort_values(by=['Global_Sales'], ascending=False)

fig, ax = plt.subplots(figsize=(6, 8))

sns.barplot(x="Platform", y="Global_Sales", data= sales_price_platform)
plt.xticks(rotation = 90)

ax.set_title('Global Sales by Platform')

ax.set_ylabel('Global Sales')

plot4_filename = 'Seaborn Barchart'

fig.savefig(project_dir + plot4_filename)


#%%

# Sales by Publisher

sales_publisher = df_videogame.groupby(['Publisher', 'Year']).Global_Sales.count()

disney = sales_publisher.loc['Disney Interactive Studios']

activision = sales_publisher.loc['Activision']

ea = sales_publisher.loc['Electronic Arts']

capcom = sales_publisher.loc['Capcom']

labels = ['disney', 'activision', 'electronic arts', 'capcom']

fig, ax = plt.subplots(figsize=(6,8))

sns.lineplot(disney.index, disney.values, data = sales_publisher)

sns.lineplot(activision.index, activision.values, data = sales_publisher)

sns.lineplot(ea.index, ea.values, data = sales_publisher)

sns.lineplot(capcom.index, capcom.values, data = sales_publisher)

ax.set_title('Sales by Publisher')

ax.set_ylabel('Sales')

ax.set_xlabel('Year')

ax.legend(labels)

plot5_filename = 'Seaborn Linechart '

fig.savefig(project_dir + plot5_filename)

