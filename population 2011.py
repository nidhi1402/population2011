#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


df = pd.read_excel('pop3.xlsx')


# In[9]:


df.describe()


# In[36]:


bracket =[0,50,100,200,250]


# In[37]:


pop =df['Population']


# In[42]:


plt.hist(x= "pop",y ="bracket",rwidth=0.8)


# In[43]:


sns.histplot(data=population, x="pop", bins=30)


# In[ ]:




