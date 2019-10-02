#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[78]:


P = np.array([[1, 2, 1, 2, 1], [3, 3, 2, 2, 1]])
Q = np.array([[5, 4, 5, 4, 5], [-1, -2, -2, -3, -3]])


# Step 1:

# In[79]:


w = np.ones(len(P[0]))
p = np.zeros((2,1))
q = np.zeros((2,1))

for i in range(len(w)):
    p += (w[i]*P[:,i]).reshape((2,1))
    q += (w[i]*Q[:,i]).reshape((2,1))

p /= np.sum(w)
q /= np.sum(w)
print(p)


# Step 2:

# In[80]:


A = P - p
B = Q - q


# In[81]:


print(A)
print(np.diag(w))
print(B)
S = A.dot(np.diag(w)).dot(B.T)


# In[82]:


print(S)


# In[83]:


U,Sigma,V = np.linalg.svd(S)


# In[84]:


rectifier = np.ones(len(V))
print(np.linalg.det(V.dot(U.transpose())))
rectifier[-1] = -1
R = V.dot(U.T)


# In[85]:


print(R)


# In[86]:


t = q - R.dot(p)


# In[87]:


print(R.dot(p))
print(q)


# In[88]:


print((R.dot(P)))


# In[89]:


plt.scatter(x=P[0], y=P[1])
plt.scatter(x=p[0], y=p[1])
plt.scatter(x=Q[0], y=Q[1])
plt.scatter(x=q[0], y=q[1])
plt.scatter(x=(R.dot(P))[0], y=(R.dot(P))[1])
plt.scatter(x=(R.dot(p))[0], y=(R.dot(p))[1])
plt.show()


# In[ ]:





# In[ ]:




