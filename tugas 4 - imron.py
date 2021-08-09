#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world!")
print ("salam dari Imron rosadi")# mode skrip


# In[2]:


height = 1.84


# In[3]:


tall = True


# In[4]:


height1 = 1.84
height2 = 1.79
height3 = 1.82
height4 = 1.90


# In[5]:


[1.84, 1.79, 1.82, 1.90, 1.80]


# In[6]:


height = [1.84, 1.79, 1.82, 1.90, 1.80]


# In[7]:


height


# In[8]:


famz = ["Abe", 1.84, "Beb", 1.79, "Cory", 1.82, "Dad", 1.90]


# In[9]:


famz


# In[10]:


#Solusi: NumPy
import numpy as np


# In[11]:


np_height = np.array(height)


# In[12]:


np_height 


# In[14]:


weight = [66.5, 60.3, 64.7, 89.5, 69.8] 


# In[15]:


np_weight = np.array(weight)


# In[16]:


np_weight


# In[17]:


bmi = np_weight / np_height ** 2


# In[18]:


bmi


# In[19]:


np_height = np.array([1.84, 1.79, 1.82, 1.9, 1.8])
np_weight = np.array([66.5, 60.3, 64.7, 89.5, 69.8])


# In[20]:


type(np_height)
type(np_weight)


# In[21]:


np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])


# In[22]:


np_2d


# In[23]:


np_2d.shape


# In[24]:


#SciPy dan Pandas Pandas (Panel Data) merupakan library popular di Python yang digunakan untuk data structure dan data analysis
np.array([1, 2, 3, 4, 5])


# In[25]:


np.array([[1, 2], [3, 4]])


# In[26]:


import pandas as pd
Tab = pd.read_csv("Tab.csv")
Tab


# In[27]:


Tab.Negara


# In[28]:


Tab.Populasi


# In[29]:


# Matplotlib Matplotlib adalah library Python untuk visualisasi data dengan dua dimensi

import matplotlib.pyplot as plt
year = [1980, 1990, 2000, 2010, 2020]
price = [2.5, 7.6, 9.7, 15.8, 22.9]


# In[30]:


plt.plot(year, price)
plt.show()


# In[31]:


plt.scatter(year,price)


# In[32]:


plt.bar(year,price)


# In[ ]:




