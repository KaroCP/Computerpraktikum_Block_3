'''
The "Main" function of the Project. Here the user starts the plot.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
from function import Fractal


# In[2]

f, f_diff = lambda x: x**3-1, lambda x:2*x**2
f_0 = [1,-1/2+np.sqrt(3)*1J/2, -1/2-np.sqrt(3)*1J/2]
# f = Fractal(f, f_diff, f_0)
# g = Fractal(np.sin)


# In[3]

game = True
zoom = 1
translation = 0
# while game:
# print(plot(f,zoom,translation))


# In[10]

g = lambda x:x**2-1
# g = lambda a,b:[a**2-b**2-1,2*a*b]
g_diff = lambda a,b:[[2*a,-2*b],[2*b,2*a]]
g_0 = [[1,0],[-1,0]]
g = Fractal(g,g_diff,g_0)
g.max_iteration = 15
print(g.color_newton(2,[-1/2,-1/2]))


# In[11]

h1 = lambda z:z**3-1
h = lambda a,b:[np.real(h1(a+b*1J)),np.imag(h1(a+b*1J))]
# h = lambda a,b: np.array([a**3-3*a*b**2-1, 3*a**2*b-b**3])
h_diff = lambda a,b:[[3*a**2-3*b**2,-6*a*b], [6*a*b,3*a**2-3*b**2]]
h_0 = [[1,0], [-1/2,np.sqrt(3)/2],[-1/2,-np.sqrt(3)/2]]
h = Fractal(h1,h_diff,h_0)
h.max_iteration = 20
# h.density = 
print(h.color_newton(2))


# In[12]

g = lambda x:x**2+1
# g = lambda a,b:[a**2-b**2+1,2*a*b]
g_diff = lambda a,b:[[2*a,-2*b],[2*b,2*a]]
g_0 = [[0,1],[0,-1]]
g = Fractal(g,g_diff,g_0)
g.max_iteration = 10
print(g.color_newton(4,[-1/2,-1/2]))


# In[13]

# g = lambda x:x^3-1
# g_diff = lambda x:3*x^2
# g_0 = [1,-1/2+np.sqrt(3)*1J/2, -1/2-np.sqrt(3)*1J/2]

