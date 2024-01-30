'''
Reused plot_stuff.
Now a collection for data.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np


# In[2]

def get_natural(string):
    print(string)
    while True:
        number = input(" > ")
        try: 
            number = int(number)
            if number >= 1: 
                break
        except: pass
    return number
    

def catch(func, *args, handle=None):
    # handle=lambda e:np.array([[np.infty,np.infty],[np.infty,np.infty]])
    try: return func(*args)
    except Exception as e: 
        # print(e) #TODO
        return handle
    

# In[3]

def chose_fractal_x_times_n():
    print("""
You can assemble the plot information by yourself.
To simplify we consider functions like x^n-1.
They usually induce a fractal structure""")
    n = get_natural("""==================================================
First chose the power n.""")
    dens = get_natural("""
==================================================
Now say the density of the pixel.""")
    max_iter = get_natural("""
==================================================
Last enter the maximum number of iterations.""")
    print("""
Please wait now. Your fractal will be assembled.""")
    f = lambda z:z**n-1
    diff = lambda z:n*z**(n-1)
    zeta = np.exp(2*np.pi*1J/n) # primitive n-th unit root.
    # roots = np.fromfunction(lambda k:[np.real(np.power(zeta,k)),
    #                                   np.imag(np.power(zeta,k))],(n,))
    # roots = np.array(roots).T
    roots = np.array([[np.real(np.power(zeta,k)),
                      np.imag(np.power(zeta,k))] for k in range(n)])
    label = "x^{}-1".format(n)
    return f,diff,label,dens,max_iter
    
 


# In[5] 
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
            [f4_func, f4_diff, f4_0, "x**5-1", 60,30],
            [f4_func, f4_diff, f4_0, "x**5-1", 200,50]]

# In[5]

f1_func = lambda z:z**3-1
f1_diff = lambda z:3*z**2
f1_label = "x**3-1"

f2_func = lambda z:z**3-z
f2_diff = lambda z:3*z**2-1
f2_label = "x**3-x"

f4_func = lambda z:(z**2-1)/z
f4_diff = lambda z:1/z**2+1 # (2*z**2-z**2+1)/z**2
f4_label = "(x**2-1)/x"

f5_func = lambda z:1/z+z**2
f5_diff = lambda z:-1/z**2+2*z
f5_label = "1/z+z**2"

f6_func = lambda z:np.sin(z)
f6_diff = lambda z:np.cos(z)
f6_label = "sin(x)"

f7_func = lambda z:np.sin(1/z)
f7_diff = lambda z:-np.cos(1/z)/z**2
f7_label = "sin(1/x)"

f3_func = lambda z:1/z-1
f3_diff = lambda z:-1/z**2
f3_label = "1/x-1"

f8_func = lambda z:np.log(z)
f8_diff = lambda z:1/z
f8_label = "log(x)"

f9_func = lambda z:np.exp(-z)-1
f9_diff = lambda z:-np.exp(-z)
f9_label = "e^(-x)-1"

data_set = [[f1_func, f1_diff, f1_label],
            [f2_func, f2_diff, f2_label],
            [f4_func, f4_diff, f4_label],
            [f5_func, f5_diff, f5_label],
            [f9_func, f9_diff, f9_label],
            [f6_func, f6_diff, f6_label],
            [f7_func, f7_diff, f7_label],
            [f8_func, f8_diff, f8_label],
            [f3_func, f3_diff, f3_label]]

# In[6]

def choose_fractal_from_data():
    print("""
You can assemble the plot information by yourself.
To simplify we consider given functions see data_collection.
They are just test.""")
    n = get_natural("""==================================================
First chose the number of data. There is
"""+"\n".join([str(i+1)+") "+data_set[i][2] for i in range(len(data_set))]))
    dens = get_natural("""
==================================================
Now say the density of the pixel.""")
    max_iter = get_natural("""
==================================================
Last enter the maximum number of iterations.""")
    print("""
Please wait now. Your fractal will be assembled.""")
    return *data_set[n-1],dens,max_iter
        


# In[10]

import sympy


# In[100]
