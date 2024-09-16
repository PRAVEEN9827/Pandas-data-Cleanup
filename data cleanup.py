#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('D:/Data for Loans.csv')
print(df)


# In[47]:




res = (df["home_ownership"] == "MORTGAGE") &  (df['home_ownership_cat'] == 3)
df[res]





         


# In[71]:


res =(df['annual_inc'].isna())
df[res]


# In[73]:


df['annual_inc'].dropna()


# In[74]:


df


# In[96]:


reg =  df["home_ownership"].isna()
df2 = df[reg]
df.drop(df[reg].index, inplace=True)
df


# In[ ]:




