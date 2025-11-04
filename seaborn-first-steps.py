#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-04T07:40:45.239Z
"""

# # 📈 SeaBorn Library


# # 🔍 Types
# * [Bar Plot](#1)
# * [Point Plot](#6)
# * [Joint Plot](#7)
# * [Pie Chart](#8)
# * [Lm Plot](#9)
# * [Kde Plot](#10)
# * [Violin Plot](#11)
# * [Heatmap](#12)
# * [Box Plot](#13)
# * [Swarm Plot](#14)
# * [Pair Plot](#15)
# * [Count Plot](#16)


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
%matplotlib inline
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import warnings
warnings.filterwarnings('ignore') 

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

# # 📂 Data
# * MedianHouseholdIncome2015
# * PercentagePeopleBelowPovertyLevel: Proportion of people below the poverty line
# * PercentOver25CompletedHighSchool: The rate of high school graduates among people over 25 years of age
# * PoliceKillingsUS: People killed by police
# * ShareRaceByCity : City populations by race


# Read datas

median_house_hold_in_come = pd.read_csv(r"/kaggle/input/seaborn-tutorial-datasets/MedianHouseholdIncome2015.csv", encoding="windows-1252")
percentage_people_below_poverty_level = pd.read_csv(r"/kaggle/input/seaborn-tutorial-datasets/PercentagePeopleBelowPovertyLevel.csv", encoding="windows-1252")
percent_over_25_completed_highSchool = pd.read_csv(r"/kaggle/input/seaborn-tutorial-datasets/PercentOver25CompletedHighSchool.csv", encoding="windows-1252")
share_race_city = pd.read_csv(r"/kaggle/input/seaborn-tutorial-datasets/ShareRaceByCity.csv", encoding="windows-1252")
kill = pd.read_csv(r"/kaggle/input/seaborn-tutorial-datasets/PoliceKillingsUS.csv", encoding="windows-1252")

# <a id = "1"></a>
# ## Bar Plot
# * [Bar Plot 1](#2)
# * [Bar Plot 2](#3)
# * [Bar Plot 3](#4)
# * [Bar Plot 4](#5)


# <a id = "2"></a>
# ### Bar Plot 1


percentage_people_below_poverty_level.head()

percentage_people_below_poverty_level.info()

percentage_people_below_poverty_level.poverty_rate.value_counts()

area_list = (percentage_people_below_poverty_level["Geographic Area"].unique())
area_list

len(percentage_people_below_poverty_level["Geographic Area"].unique())

percentage_people_below_poverty_level.poverty_rate.replace(["-"],0.0,inplace=True)
percentage_people_below_poverty_level.poverty_rate = percentage_people_below_poverty_level.poverty_rate.astype(float)

area_poverty_ratio = []
for i in area_list:
    x = percentage_people_below_poverty_level[percentage_people_below_poverty_level["Geographic Area"] == i]
    area_poverty_rate = sum(x.poverty_rate)/len(x)
    area_poverty_ratio.append(area_poverty_rate)

data = pd.DataFrame({'area_list': area_list,'area_poverty_ratio':area_poverty_ratio})
new_index = (data['area_poverty_ratio'].sort_values(ascending=False)).index.values
sorted_data = data.reindex(new_index)

plt.figure(figsize=(16,10))
sns.barplot(x=sorted_data["area_list"], y=sorted_data["area_poverty_ratio"])
plt.xticks(rotation=45)
plt.xlabel('States')
plt.ylabel('Poverty Rate')
plt.title('Poverty Rate Given States')


# <a id = "3"></a>
# ### Bar Plot 2


kill.head()

kill.info()

kill["name"].value_counts()

seperate = kill.name[kill.name !="TK TK"].str.split()
a,b=zip(*seperate)
name_list = a + b # hem isim ya da soy isim
name_count = Counter(name_list)
most_common_names = name_count.most_common(15)
x,y = zip(*most_common_names)
x,y = list(x) , list(y)

plt.figure(figsize=(10,10))
sns.barplot(x = x, y = y, palette = sns.cubehelix_palette(len(x)))
plt.xticks(rotation = 90)
plt.xlabel("Most Common Names")
plt.ylabel("Count")
plt.title('Most common 15 Name or Surname of killed people')

name_count.most_common(15)

# <a id = "4"></a>
# ### Bar Plot 3


percent_over_25_completed_highSchool.head()

percent_over_25_completed_highSchool.info()

percent_over_25_completed_highSchool.percent_completed_hs.value_counts()

percent_over_25_completed_highSchool.percent_completed_hs.replace(["-"],0.0,inplace=True)
percent_over_25_completed_highSchool.percent_completed_hs = percent_over_25_completed_highSchool.percent_completed_hs.astype(float)

area_list = (percent_over_25_completed_highSchool["Geographic Area"].unique())
area_highschool = []

for i in area_list:
    x = percent_over_25_completed_highSchool[percent_over_25_completed_highSchool['Geographic Area']==i]
    area_highschool_rate = sum(x.percent_completed_hs)/len(x)
    area_highschool.append(area_highschool_rate)

data = pd.DataFrame({"area_list": area_list,"area_highschool_ratio": area_highschool})
new_index = (data["area_highschool_ratio"].sort_values(ascending=True)).index.values
sorted_data2 = data.reindex(new_index)

plt.figure(figsize=(20,10))
sns.barplot(x=sorted_data2["area_list"],y=sorted_data2["area_highschool_ratio"])
plt.xticks(rotation= 45)
plt.xlabel("States")
plt.ylabel("High School Graduate Rate")
plt.title("Percentage of Given State's Population Above 25 that Has Graduated High School")

x = percent_over_25_completed_highSchool[percent_over_25_completed_highSchool['Geographic Area']==i]
x

# <a id = "5"></a>
# ### Bar Plot 4


share_race_city.head()

share_race_city.info()

# share_race_city.City
# share_race_city.share_white
# share_race_city.share_white.value_counts()
# share_race_city.share_hispanic.value_counts()
# .
# .
# .
# share_race_city["Geographic area"].unique()
# share_race_city["City"].unique()
len(share_race_city["City"].unique())

share_race_city.replace(['-'],0.0,inplace = True)
share_race_city.replace(['(X)'],0.0,inplace = True)

share_race_city.loc[:,['share_white','share_black','share_native_american','share_asian','share_hispanic']] = share_race_city.loc[:,['share_white','share_black','share_native_american','share_asian','share_hispanic']].astype(float)
area_list = list(share_race_city["Geographic area"].unique())

share_white = []
share_black = []
share_native_american = []
share_asian = []
share_hispanic = []

for i in area_list:
    x = share_race_city[share_race_city["Geographic area"] == i]
    share_white.append(sum(x.share_white)/len(x))
    share_black.append(sum(x.share_black)/len(x))
    share_native_american.append(sum(x.share_native_american)/len(x))
    share_asian.append(sum(x.share_asian)/len(x))
    share_hispanic.append(sum(x.share_hispanic)/len(x))


f,ax = plt.subplots(figsize = (9,15))
sns.barplot(x=share_white , y=area_list,color="green",alpha = 0.5,label='White')
sns.barplot(x=share_black , y=area_list,color="blue",alpha = 0.7,label='African American')
sns.barplot(x=share_native_american , y=area_list,color="cyan",alpha = 0.6,label='Native American')
sns.barplot(x=share_asian , y=area_list,color="yellow",alpha = 0.6,label='Asian')
sns.barplot(x=share_hispanic , y=area_list,color="red",alpha = 0.6,label='Hispanic')

ax.legend(loc='lower right',frameon = True)     # legendlarin gorunurlugu
ax.set(xlabel='Percentage of Races', ylabel='States',title = "Percentage of State's Population According to Races ")

# <a id = "6"></a>
# ## Point Plot


sorted_data['area_poverty_ratio'] = sorted_data['area_poverty_ratio'] / sorted_data['area_poverty_ratio'].max()
sorted_data2['area_highschool_ratio'] = sorted_data2['area_highschool_ratio'] / sorted_data2['area_highschool_ratio'].max()

data = pd.concat([sorted_data,sorted_data2['area_highschool_ratio']],axis=1)
data.sort_values('area_poverty_ratio',inplace=True)

f,ax1 = plt.subplots(figsize=(20,10))
sns.pointplot(x="area_list",y="area_poverty_ratio",data=data,color = "lime")
sns.pointplot(x="area_list", y="area_highschool_ratio",data=data, color = "red")
plt.text(40,0.6,'high school graduate ratio',color='red',fontsize = 17,style = 'italic')
plt.text(40,0.55, "poverty  ratio", color = "lime",fontsize = 18 , style = "italic")
plt.xlabel('States',fontsize = 15,color='blue')
plt.ylabel('Values',fontsize = 15,color='blue')
plt.title('High School Graduate  VS  Poverty Rate',fontsize = 20,color='blue')
plt.grid()

# <a id = "7"></a>
# ## Joint Plot


data.head()

# Visualization of high school graduation rate vs Poverty rate of each state with different style of seaborn code
# joint kernel density
# pearsonr= if it is 1, there is positive correlation and if it is, -1 there is negative correlation.
# If it is zero, there is no correlation between variables
# Show the joint distribution using kernel density estimation 

g = sns.jointplot(data=data, x='area_poverty_ratio', y='area_highschool_ratio', 
                  kind="kde", height=6, fill=True, cmap="Blues")

data.head()

# you can change parameters of joint plot
# kind : { “scatter” | “reg” | “resid” | “kde” | “hex” }
# Different usage of parameters but same plot with previous one

g = sns.jointplot(data=data ,x='area_poverty_ratio', y='area_highschool_ratio',
                 height=6,ratio = 3, color="#FF0000")

# <a id = "8"></a>
# ## Pie Chart


kill.race.head(15)

kill.race.value_counts()

# Race rates according in kill data

kill.race.dropna(inplace=True)
labels = kill.race.value_counts().index
colors = ['grey','blue','red','yellow','green','brown']
explode = [0,0,0,0,0,0]
sizes = kill.race.value_counts().values

# visual
plt.figure(figsize = (7,7))
plt.pie(sizes ,explode = explode, labels=labels, colors = colors
       , autopct='%1.1f%%')
plt.title("Killed People According to Races", color = 'blue' ,fontsize = 15)

# <a id = "9"></a>
# ## Lm Plot


data.head()

# Visualization of high school graduation rate vs Poverty rate of each state with different style of seaborn code
# lmplot 
# Show the results of a linear regression within each dataset

sns.lmplot(data=data, x="area_poverty_ratio", y="area_highschool_ratio")

# <a id = "10"></a>
# ## Kde Plot


data.head()

# Visualization of high school graduation rate vs Poverty rate of each state with different style of seaborn code
# cubehelix plot

sns.kdeplot(data=data,x="area_poverty_ratio" , y="area_highschool_ratio", fill=True, cut=3, thresh=0, cmap='Blues')

# <a id = "11"></a>
# ## Violin Plot


data.head()

# Show each distribution with both violins and points
# Use cubehelix to get a custom sequential palettz

pal = sns.cubehelix_palette(2, rot=-.5, dark=.3)
sns.violinplot(data=data, palette=pal, inner="points")

# <a id = "12"></a>
# ## Heatmap


correlationnn1 = data.corr(numeric_only=True)
print(correlationnn1)

#correlation map
# Visualization of high school graduation rate vs Poverty rate of each state with different style of seaborn code

f, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(data.select_dtypes(include=['number']).corr(), 
            annot=True, 
            linewidths=0.5,
            linecolor="red", 
            fmt='.1f',
            ax=ax)

# <a id = "13"></a>
# ## Box Plot


kill.head()

kill.manner_of_death.unique()

# manner of death(olum sekli) : ates edilerek, ates edilerek ve sok tabancasiyla
# gender cinsiyet
# age: yas
# Plot the orbital period with horizontal boxes

sns.boxplot(x="gender", y="age", hue="manner_of_death", data=kill, palette="PRGn")

# <a id = "14"></a>
# ## Swarm Plot


kill.head()

# swarm plot
# manner of death(olum sekli) : ates edilerek, ates edilerek ve sok tabancasiyla
# gender cinsiyet
# age: yas

plt.figure(figsize=(10, 6))
sns.swarmplot(data=kill, x="gender", y="age", hue="manner_of_death")
plt.title("Age Distribution by Gender and Manner of Death", fontsize=14)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Age", fontsize=12)
plt.legend(title="Manner of Death", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# <a id = "15"></a>
# ## Pair Plot


data.head()

# pair plot

sns.pairplot(data)

# <a id = "16"></a>
# ## Count Plot


kill.gender.value_counts()

kill.head()

# kill properties
# Manner of death

#sns.countplot(x=kill['gender'])

sns.countplot(x= kill["manner_of_death"])

plt.title("Manner of Death",color = 'blue',fontsize=15)

# kill weapon

armed = kill.armed.value_counts()
#print(armed)

plt.figure(figsize=(10,7))
sns.barplot(x=armed[:7].index,y=armed[:7].values)
plt.ylabel('Kill Number of Weapon')
plt.xlabel('Weapon Types')
plt.title('Kill weapon',color = 'blue',fontsize=15)

armed

# age of killed people

age_list =['above 25' if i >= 25 else 'below 25' for i in kill.age]
df = pd.DataFrame({'age':age_list})
sns.countplot(x=df.age)
plt.ylabel('Number of Killed People')
plt.title('Age of killed people',color = 'blue',fontsize=15)

# Race of killed people

sns.countplot(data=kill, x='race')
plt.title('Race of killed people',color = 'blue',fontsize=15)

# Most dangerous cities

city = kill.city.value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=city[:12].index,y=city[:12].values)
plt.xticks(rotation=45)
plt.ylabel('Number of Killed People')
plt.xlabel('Cities')
plt.title('Most dangerous cities',color = 'blue',fontsize=15)

city

# most dangerous states

state = kill.state.value_counts()
plt.figure(figsize=(10,7))
sns.barplot(x=state[:20].index,y=state[:20].values)
plt.ylabel('Number of Killed People')
plt.xlabel('States')
plt.title('Most dangerous state',color = 'blue',fontsize=15)

state.head(10)

# Having mental ilness or not for killed people

sns.countplot(x=kill["signs_of_mental_illness"])
plt.xlabel('Having Mental illness')
plt.ylabel('Number of Mental illness')
plt.title('Having mental illness or not',color = 'blue', fontsize = 15)

# They are all mentally healty

# Threat types

kill.threat_level.head(15)

# Threat types

kill.threat_level.value_counts()

# Threat types

sns.countplot(x=kill["threat_level"])
plt.xlabel('Threat Types')
plt.ylabel('Number of Killed People')
plt.title('Threat types',color = 'red', fontsize = 15)

# Flee types

sns.countplot(x=kill["flee"])
plt.xlabel('Flee Types')
plt.ylabel('Number of Killed People')
plt.title('Flee types',color = 'blue', fontsize = 15)

# Having body cameras or not for police

sns.countplot(x=kill["body_camera"])
plt.xlabel('Having Body Cameras')
plt.ylabel('Number of Killed People')
plt.title('Having body cameras or not on Police',color = 'blue',fontsize = 15)

kill.body_camera.unique()

# Kill numbers from states in kill data

sta = kill.state.value_counts().index[:10]
sns.barplot(x=sta,y = kill.state.value_counts().values[:10])
plt.ylabel('Number of Killed People')
plt.xlabel('States')
plt.title('Kill Numbers from States',color = 'blue',fontsize=15)

# # 🎯 Conclusion
# 
# In this study, we comprehensively learned the fundamental visualization techniques of the **Seaborn** library.
# 
# ## 💡 What Did We Do?
# 
# ### Data Processing
# - Data cleaning and preprocessing
# - Filling missing data
# - Working with data types
# - Working with multiple datasets
# 
# ### Visualization Techniques
# - **Bar Plot**: Comparison of categorical data
# - **Point Plot**: Trend analysis with point graphs
# - **Joint Plot**: Relationship between two variables
# - **Pie Chart**: Percentage distributions
# - **Lm Plot**: Regression analysis
# - **Kde Plot**: Density distribution
# - **Violin Plot**: Distribution and density visualization
# - **Heatmap**: Correlation matrix analysis
# - **Box Plot**: Outlier detection
# - **Swarm Plot**: Categorical data distribution
# - **Pair Plot**: Multivariate relationships
# - **Count Plot**: Frequency analysis
# 
# 
# 
# 
# 
# 
# Thank you for making it to the end.
# 


# # 📖 References
# - Udemy Course: Da by DATAI TEAM
# - Kaggle Notebook: [Seaborn Tutorial for Beginners](https://www.kaggle.com/code/kanncaa1/seaborn-tutorial-for-beginners)