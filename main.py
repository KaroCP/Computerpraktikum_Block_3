#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
from plot_stuff import plot
from function import Function


# In[2]

f, f_diff = lambda x: x**3-1, lambda x:2*x**2
f_0 = [1,-1/2+np.sqrt(3)*1J/2, -1/2-np.sqrt(3)*1J/2]
f = Function(f, f_diff, f_0)
# g = Function(np.sin)


# In[3]

game = True
zoom = 1
translation = 0
# while game:
print(plot(f,zoom,translation))

