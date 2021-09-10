#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Import Libraries-Importar Librerías 


# In[42]:


import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 
import scipy


# In[ ]:


#Data Preprocessing-Procesamiento de Datos


# In[43]:


df=pd.read_csv('Amazon_Best_Seller_2021_June.csv',index_col="Category")
df_filtrado=df.fillna(0)
print(df.keys())
print(df['Product Link'])


# In[9]:


df.nunique()


# In[11]:


df.shape


# In[12]:


df.describe()


# In[14]:


df.isnull().sum()


# In[15]:


df = df.drop(['Product Link'], axis=1)


# In[16]:


df


# In[18]:


df['Reviews Count'] = df['Reviews Count'].replace(',','', regex=True)


# In[20]:


df['Price'] = df['Price'].str.replace('$','', regex=True)


# In[22]:


df['Rank'] = df['Rank'].str.replace('#','', regex=True)
df


# In[23]:


df['No of Sellers'] = df['No of Sellers'].str.replace(' Sellers','', regex=True)
df


# In[32]:


df['No of Sellers'] = df['No of Sellers'].astype(int)
df['Rank'] = df['Rank'].astype(float)
df['Reviews Count'] = df['Reviews Count'].astype(int)
df['Price'] = df['Price'].astype(float)


# In[ ]:


#Data Visualizations-Visualización de datos
#Univariate Analysis-Análisis Invariado


# In[8]:


df['Rating'].value_counts()


# In[14]:


sns.histplot(df['Rating'])


# In[15]:


df['Rating'].value_counts().plot.pie()
plt.show()


# In[ ]:


#Bivariate Analysis-Análisis bivariado


# In[5]:


sns.boxplot(x=df['Rating'])


# In[ ]:


#As expected, the higher ratings are more frequent in the dataset, though 4.9 and 5.0 is less frequent than expected but this is most likely due to the scarcity of these ratings


# In[6]:


df['No of Sellers'].value_counts()


# In[7]:


sns.histplot(df['No of Sellers'])


# In[12]:


df['No of Sellers'].value_counts().plot.pie()
plt.show()


# In[15]:


df['Price'].value_counts()


# In[16]:


sns.histplot(df['Price'])


# In[17]:


df['Price'].value_counts().plot.pie()
plt.show()


# In[26]:


sns.pairplot(data=df)


# In[ ]:


#We are going to analyze the relation of each data point to price and rating


# In[37]:


sns.boxplot(x=df['Rating'], y=df['Price'])


# In[38]:


df.groupby('Rank')['Price'].describe()


# In[49]:


sns.boxplot(x=df['Reviews Count'], y=df['Rating'])


# In[51]:


df.groupby('Category')['Rating'].describe()


# In[52]:


sns.boxplot(x=df['Price'], y=df['Rating'])


# In[56]:


df.groupby('Price')['No of Sellers'].describe()


# In[54]:


sns.boxplot(x=df['No of Sellers'], y=df['Rating'])


# In[55]:


df.groupby('Rating')['No of Sellers'].describe()

