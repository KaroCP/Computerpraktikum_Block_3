'''
Reused plot_stuff.
Now a collection for data. #TODO Shift this into csv data?
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np


# In[2] 
# create some exampels

f1_func = lambda z:z**2-1  # lambda a,b:[a**2-b**2-1,2*a*b]
f1_diff = lambda z:2*z     # lambda a,b:[[2*a,-2*b],[2*b,2*a]]
f1_0 = [[1,0],[-1,0]]

f2_func = lambda z:z**2+1  # lambda a,b:[a**2-b**2+1,2*a*b]
f2_diff = lambda z:2*z     # lambda a,b:[[2*a,-2*b],[2*b,2*a]]
f2_0 = [[0,1],[0,-1]]

f3_func = lambda z:z**3-1  # lambda a,b: np.array([a**3-3*a*b**2-1, 3*a**2*b-b**3])
f3_diff = lambda z:3*z**2  # lambda a,b:[[3*a**2-3*b**2,-6*a*b], [6*a*b,3*a**2-3*b**2]]
f3_0 = [[1,0], [-1/2,np.sqrt(3)/2],[-1/2,-np.sqrt(3)/2]]

f4_func = lambda z:z**5-1  # lambda a,b: np.array([a**5-10*a**3*b**2+5*a*b**4-1, 5*a**4*b-10*a**2*b**3+b**5])
f4_diff = lambda z:5*z**4  # lambda a,b:[[5*a**4-5*6*a**2*b**2+5*b**4,     -5*4*a**3*b+5*4*a*b**3], 
                           #             [20*a**3*b-20*a*b**3,         5*a**4-30*a**2*b**2+5*b**4]]
f4_0 = [[1,0], [(-1+np.sqrt(5))/4, np.sqrt((5+np.sqrt(5))/8)],
               [(-1-np.sqrt(5))/4, np.sqrt((5-np.sqrt(5))/8)],
               [(-1-np.sqrt(5))/4,-np.sqrt((5-np.sqrt(5))/8)],
               [(-1+np.sqrt(5))/4,-np.sqrt((5+np.sqrt(5))/8)],]

# Fractal(function, derivative, roots, label, density, max iteration level, tolerance)
data_set = [[f1_func, f1_diff, f1_0, "x**2-1", 10,10],
            [f2_func, f2_diff, f2_0, "x**2+1", 20,10],
            [f3_func, f3_diff, f3_0, "x**3-1", 20,10],
            [f3_func, f3_diff, f3_0, "x**3-1", 50,20],
            [f4_func, f4_diff, f4_0, "x**5-1", 50,60]]

# In[3]

def choose_fractal():
    print("""
========================================
First chose the function, which will be used to create the fractal.
Input a number between 1 and 5 to choose.""")
    while True:
        string = input(" > ")
        try: 
            string = int(string)
            if string in [1,2,3,4,5]: 
                break
        except: pass
    return data_set[string-1]
        


# In[10]



# In[100]
