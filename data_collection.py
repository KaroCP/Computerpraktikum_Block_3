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
        

# In[3]

def chose_fractal_x_times_n():
    print("""
You can assemble the plot information by yourself.
To simplify we consider functions like x^n-1.
They usually induce a fractal structure""")
    n = get_natural("""==================================================
Please chose the power n.""")
    print("Please wait now. Your fractal will be assembled.\n ")
    f = lambda z:z**n-1
    diff = lambda z:n*z**(n-1)
    label = "x^{}-1".format(n)
    return f,diff,label
    

# In[4]

f1_func = lambda z:z**3-1
f1_diff = lambda z:3*z**2
f1_label = "x^3-1"

f2_func = lambda z:z**3-z
f2_diff = lambda z:3*z**2-1
f2_label = "x^3-x"

f10_func = lambda z:z**4-z**2+1
f10_diff = lambda z:4*z**3-2*z
f10_label = "x^4-x^2+1"

f11_func = lambda z:z**12-1
f11_diff = lambda z:12*z**11
f11_label = "x^12-1"

f4_func = lambda z:(z**2-1)/z
f4_diff = lambda z:1/z**2+1 # (2*z**2-z**2+1)/z**2
f4_label = "(x^2-1)/x"

f5_func = lambda z:1/z+z**2
f5_diff = lambda z:-1/z**2+2*z
f5_label = "1/z+z^2"

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

data_set = [[ f1_func,  f1_diff,  f1_label],
            [ f2_func,  f2_diff,  f2_label],
            [f10_func, f10_diff, f10_label],
            [f11_func, f11_diff, f11_label],
            [ f4_func,  f4_diff,  f4_label],
            [ f5_func,  f5_diff,  f5_label],
            [ f9_func,  f9_diff,  f9_label],
            [ f6_func,  f6_diff,  f6_label],
            [ f7_func,  f7_diff,  f7_label],
            [ f8_func,  f8_diff,  f8_label],
            [ f3_func,  f3_diff,  f3_label]]

# In[5]

def choose_fractal_from_data():
    print("""
You can assemble the plot information by yourself.
To simplify we consider given functions see data_collection.
They are just test.""")
    n = get_natural("""==================================================
Please chose the number of data. There are
"""+"\n".join([str(i+1)+") "+data_set[i][2] for i in range(len(data_set))]))
    print("""
Please wait now. Your fractal will be assembled.""")
    return data_set[n-1]
        


# In[10]


# In[100]
