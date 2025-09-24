import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.colors import rgb2hex
import matplotlib.cm as cm


import matplotlib.colors
from collections import Counter
cmap2 = cm.get_cmap('twilight',13)
colors1= []
for i in range(cmap2.N):
    rgb= cmap2(i)[:4]
    colors1.append(rgb2hex(rgb))

# Set style
sns.set(style='whitegrid')

#Data loading and preprocessing
df= pd.read_csv("Data/pokemon.csv")

#Get the information about the data
df.info()

#Getting columns info
df.columns

#Statitical summary of data
df.describe()

#categorical and numerical values
df.info

#Missing value analysis
df.isnull().sum()

#percentage of missing data out of the total
p = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
t = df.isnull().sum().sort_values(ascending=False)

m_data = pd.concat([t, p], axis=1, keys=['Total', 'Percent'])
m_data.head(10)

#Getting count of unique value of each column
for i in list(df.columns):
    print("{} -> {}".format(i, df[i].value_counts().shape[0]))

# Univariate analysis
# Categorical features univariate analysis
# Type 1 Pokemon Count

plt.figure(figsize=(10,8))
sns.countplot(x='Type 1',data=df,palette='mako',order = df['Type 1'].value_counts().index)
plt.xlabel('Type1')
plt.xticks(rotation = 60)
plt.ylabel('Count')
plt.legend()
plt.title('Type1 Count')

plt.show()

# Type 2 Pokemon Count
plt.figure(figsize=(10,8))
sns.countplot(x='Type 2',data=df,palette='mako',order = df['Type 2'].value_counts().index)
plt.xlabel('Type 2')
plt.xticks(rotation = 60)
plt.ylabel('Count')
plt.legend()
plt.title('Type 2 Count')

plt.show()

#Numerical features univariate analysis
# Total Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['Total'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('Total Distribution')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

# HP Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['HP'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('HP Distribution')
plt.xlabel('HP')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

# Attack Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['Attack'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('Attack Distribution')
plt.xlabel('Attack')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

# Defense Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['Defense'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('Defense Distribution')
plt.xlabel('Defense')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

# Sp Attack Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['Sp. Atk'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('Sp. Attack Distribution')
plt.xlabel('Sp. Attack')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

# Sp Defense Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['Sp. Def'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('Sp. Def Distribution')
plt.xlabel('Sp. Def')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

# Speed Distribution
plt.figure(figsize=(12,10))
sns.distplot(x=df['Speed'],bins=10,color='darkcyan',kde=True,hist=True)
plt.title('Speed Distribution')
plt.xlabel('Speed')
plt.ylabel('Frequency')
plt.xticks(rotation=45)

plt.show()

#   Name Percentage
plt.figure(figsize=(25,12))
p_r = df['Name'].value_counts().head(10)
plt.pie(x=p_r,labels=p_r.index,colors=colors1,autopct='%.0f%%',explode=[0.07 for i in p_r.index],startangle=180,wedgeprops={'linewidth':1,'edgecolor':'black'},shadow=True)
plt.title('Name percentage ')
plt.legend(loc='upper right',title='Name')

plt.show()

#   Type 1 Percentage
plt.figure(figsize=(25,12))
p_r = df['Type 1'].value_counts().head(10)
plt.pie(x=p_r,labels=p_r.index,colors=colors1,autopct='%.0f%%',explode=[0.07 for i in p_r.index],startangle=180,wedgeprops={'linewidth':1,'edgecolor':'black'},shadow=True)
plt.title('Type 1 percentage ')
plt.legend(loc='upper right',title='Type 1')

plt.show()

#   Type 2 Percentage
plt.figure(figsize=(25,12))
p_r = df['Type 2'].value_counts().head(10)
plt.pie(x=p_r,labels=p_r.index,colors=colors1,autopct='%.0f%%',explode=[0.07 for i in p_r.index],startangle=180,wedgeprops={'linewidth':1,'edgecolor':'black'},shadow=True)
plt.title('Type 2 percentage ')
plt.legend(loc='upper right',title='Type 2')

plt.show()

#   Legendary Percentage
plt.figure(figsize=(25,12))
p_r = df['Legendary'].value_counts().head(10)
plt.pie(x=p_r,labels=p_r.index,colors=colors1,autopct='%.0f%%',explode=[0.07 for i in p_r.index],startangle=180,wedgeprops={'linewidth':1,'edgecolor':'black'},shadow=True)
plt.title('Legendary percentage ')
plt.legend(loc='upper right',title='Legendary')

plt.show()