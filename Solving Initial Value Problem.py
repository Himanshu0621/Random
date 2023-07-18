#!/usr/bin/env python
# coding: utf-8

# In[3]:


from numpy import *
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# In[4]:


u0 = 3
T = 5


# In[6]:


def rhs (t, u):
    return u*(1-u)


# In[8]:


Sol = solve_ivp(rhs, [0, T], [u0], t_eval = linspace(0, T, 101))
t = Sol.t
u = Sol.y[0, :]


# In[9]:


u


# In[10]:


t


# In[12]:


plt.figure()
plt.plot(t, u, 'b-')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# In[ ]:




