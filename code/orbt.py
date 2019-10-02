#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

P = np.array([[1, 2, 1, 2, 1], [1, 3, 3, 2, 2]])
Q = np.array([[6, 4, 5, 4, 5], [-1, -2, -2, -3, -3]])

w = np.ones(len(P[0]))
w[0] = 4
p = np.zeros((2,1))
q = np.zeros((2,1))

for i in range(len(w)):
    p += (w[i]*P[:,i]).reshape((2,1))
    q += (w[i]*Q[:,i]).reshape((2,1))

p /= np.sum(w)
q /= np.sum(w)


A = P - p
B = Q - q


S = A.dot(np.diag(w)).dot(B.T)


U,Sigma,V = np.linalg.svd(S)


rectifier = np.ones(len(V))
print(np.linalg.det(V.dot(U.transpose())))
rectifier[-1] = -1
R = V.dot(U.T)

t = q - R.dot(p)

plt.scatter(x=Q[0], y=Q[1])
plt.scatter(x=q[0], y=q[1], color="g")
plt.scatter(x=(R.dot(P)+t)[0], y=(R.dot(P)+t)[1], color="r")
plt.scatter(x=(R.dot(p)+t)[0], y=(R.dot(p)+t)[1], color="g")
plt.show()