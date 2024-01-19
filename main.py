'''
The "Main" function of the Project. Here the user starts the plot.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
from function import Fractal


# In[2] #TODO

game = True
zoom = 1
translation = [0,0]
# while game:
#     f.color_newton(zoom,translation)
#     zoom = interaction1
#     translation = interaction2


# Now the exampels

# In[10]

g = lambda x:x**2-1
# g = lambda a,b:[a**2-b**2-1,2*a*b]
g_diff = lambda a,b:[[2*a,-2*b],[2*b,2*a]]
g_0 = [[1,0],[-1,0]]
g = Fractal(g,g_diff,g_0,"x**2-1")
g.max_iteration = 15
g.color_newton()


# In[11]

g = lambda x:x**2+1
# g = lambda a,b:[a**2-b**2+1,2*a*b]
g_diff = lambda a,b:[[2*a,-2*b],[2*b,2*a]]
g_0 = [[0,-1],[0,1]]
g = Fractal(g,g_diff,g_0,"x**2+1")
g.max_iteration = 10
g.color_newton()


# In[12]

h1 = lambda z:z**3-1
h = lambda a,b:[np.real(h1(a+b*1J)),np.imag(h1(a+b*1J))]
# h = lambda a,b: np.array([a**3-3*a*b**2-1, 3*a**2*b-b**3])
h_diff = lambda a,b:[[3*a**2-3*b**2,-6*a*b], [6*a*b,3*a**2-3*b**2]]
h_0 = [[1,0], [-1/2,np.sqrt(3)/2],[-1/2,-np.sqrt(3)/2]]
h = Fractal(h1,h_diff,h_0,"x**3+1")
h.max_iteration = 20
h.color_newton(2)


# In[13]

# g = lambda x:x^3-1
# g_diff = lambda x:3*x^2
# g_0 = [1,-1/2+np.sqrt(3)*1J/2, -1/2-np.sqrt(3)*1J/2]

