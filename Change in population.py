#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
from numpy import linspace, zeros
import matplotlib.pyplot as plt


# Parameters

# In[11]:


n = 40
T = 1.0
dt =  T/n
t = linspace (0, T, n+1)


# In[24]:


y = zeros(n+1)
r = 6.6
y0 = 1000


# In[25]:


y[0] = y0


# In[26]:


for k in range(n):
    y[k+1] = y[k] + r*dt*y[k]


# In[27]:


k


# In[28]:


print (y[k+1])


# In[29]:


plt.figure()
plt.plot(t, y,  'bo-')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




