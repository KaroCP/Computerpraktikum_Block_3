'''
Modul to collect data.'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
from sympy.parsing.sympy_parser import parse_expr
import sympy
from sympy import sympify


# In[2]

def get_natural(max_n=np.Inf):
    """
    Debug function which allows the user to insert a natural number equal less
    n_max. If the input wasn´t acceptable the User can try again.

    Parameters
    ----------
    max_n : int, optional
        The inclusive maximal natural number which is accepted. 
        The default is np.Inf.

    Returns
    -------
    number : int
        A natural number between 1 and n_max.
    """
    while True:
        number = input(" > ")
        try: 
            number = int(number)
            if number >= 1 and number <= max_n: 
                return number
        except: pass

def get_bool():
    """
    Debug function which allows the user to insert True or False. If the input
    wasn´t acceptable the User can try again.

    Returns
    -------
    bool
        The input of the user.
    """
    while True:
        string = input(" > ")
        if string == "True" or string == "False":
            return string == "True"


# In[3]

def chose_fractal_x_times_n():
    """
    Function to generate data for a fractal.
    Here the idea is to test functions of form x^n-1.
    """
    print("""
To simplify we consider functions like x^n-1.
They usually induce a fractal structure""")
    print("""==================================================
Please chose the power n.""")
    n = get_natural()
    func = lambda z:z**n-1
    diff = lambda z:n*z**(n-1)
    label = "x^{}-1".format(n)
    return func,diff,label
    

# In[4]

f1_func = lambda z:np.power(z,3)-1
f1_diff = lambda z:3*np.power(z,2)
f1_label = "x^3-1"

f2_func = lambda z:np.power(z,3)-1
f2_diff = lambda z:3*np.power(z,2)
f2_label = "x^3-1 with animation" 
f2_pointer = [-np.pi/np.sqrt(12),0.08]

f3_func = lambda z:1/z+z**2
f3_diff = lambda z:-1/z**2+2*z
f3_label = "1/z+z^2"

# (z-1)^2(z+1)(z-1J) = (z-i)(z-1)(z^2-1) = (z-i)(z^3-z^2-z^+1) = z^4-(1+i)z^3-(1+i)z^2+(1-i)z-i
f4_func = lambda z:np.power(z,4)-(1+1J)*np.power(z,3)-(1-1J)*z**2+(1+1J)*z-1J
f4_diff = lambda z:4*np.power(z,3)-3*(1+1J)*np.power(z,2)-2*(1-1J)*z+(1+1J)
f4_label = "(x-1)^2*(x+1)*(x-i)"  

f5_func = lambda z:z**4-z**2+1
f5_diff = lambda z:4*z**3-2*z
f5_label = "x^4-x^2+1"

f6_func = lambda z:np.power(z,7)-z
f6_diff = lambda z:7*np.power(z,6)-1
f6_label = "x^7-x"

f7_func = lambda z:np.power(z,12)-1
f7_diff = lambda z:12*np.power(z,11)
f7_label = "x^12-1"

f8_func = lambda z:np.sin(z)
f8_diff = lambda z:np.cos(z)
f8_label = "sin(x)"

f9_func = lambda z:np.exp(z)-1
f9_diff = lambda z:np.exp(z)
f9_label = "e^x-1"

f10_func = lambda z:np.exp(-2*z)-1
f10_diff = lambda z:-2*np.exp(-2*z)
f10_label = "e^(-2x)-1 with animation"
f10_pointer = [np.pi/np.exp(3)+0.001,np.sin(1)*np.sqrt(2)]

f11_func = lambda z:np.sin(1/z)
f11_diff = lambda z:-np.cos(1/z)/z**2
f11_label = "sin(1/x)"

f12_func = lambda z:np.sin(1/z)
f12_diff = lambda z:-np.cos(1/z)/z**2
f12_pointer = [0,0]
f12_label = "sin(1/x) with animation"

f13_func = lambda z:np.exp(1/z)-1
f13_diff = lambda z:-np.exp(1/z)/z**2
f13_label = "e^(1/x)-1"

f14_func = lambda z:np.log(z)
f14_diff = lambda z:1/z
f14_label = "log(x)"

data_set = [[ f1_func,  f1_diff,  f1_label],
            [ f2_func,  f2_diff,  f2_label,  f2_pointer],
            [ f3_func,  f3_diff,  f3_label],
            [ f4_func,  f4_diff,  f4_label],
            [ f5_func,  f5_diff,  f5_label],
            [ f6_func,  f6_diff,  f6_label],
            [ f7_func,  f7_diff,  f7_label],
            [ f8_func,  f8_diff,  f8_label],
            [ f9_func,  f9_diff,  f9_label],
            [f10_func, f10_diff, f10_label, f10_pointer],
            [f11_func, f11_diff, f11_label],
            [f12_func, f12_diff, f12_label, f12_pointer],
            [f13_func, f13_diff, f13_label],
            [f14_func, f14_diff, f14_label]]


def choose_fractal_from_data():
    """
    Function to generate data for a fractal.
    Here we take data from a provided set of data.
    """
    print("""
==================================================
Please chose the number of data. There are
"""+"\n".join([str(i+1)+") "+data_set[i][2] for i in range(len(data_set))]))
    n = get_natural(len(data_set)-1)
    return data_set[n-1]
        

# In[5]

def calculate_derivative(function):
    """
    Help function to calculate the derivative of a given function symbolically.

    Parameters
    ----------
    function : function
        Function from C to C which takes one complex entry.

    Returns
    -------
    function
        Function from C to C which takes one complex entry.
        The derivative of function.
    """
    return sympy.lambdify(sympy.symbols("z"),sympy.diff(parse_expr(
        str(function(sympy.symbols("z"))), transformations='all'), "z"))


def choose_any_fractal_function():
    """
    Function to generate data for a fractal.
    Here the user can insert a function in the consol.
    The derivative will be calculated symbolicaly.
    """
    print("""
Please input your function that maps z to some complex 
value, i.e. for example z^3-1""")
    temporary_bool = True
    while temporary_bool: 
        input1 = input(" > ")
        try:
            f = sympify(input1)
            print(f)
            diff = sympy.diff(f, sympy.Symbol("z"))
            label = input1
            temporary_bool = False
            print("The function parsed!")
            return sympy.lambdify(sympy.Symbol("z"), f),sympy.lambdify(sympy.Symbol("z"), diff),label
        except:
            print("Please enter a parsable expression.")


# In[6]

def get_fractal():
    print("""
You can assemble the plot information by yourself.
First you can chose whether you like to look at one
of the provided examples or enter a function by yourself.
Enter 'True' if you want to enter a function by yourself
and enter 'False' if you want to use one of the provided examples.""")
    fix_data = get_bool()
    if fix_data: data = choose_any_fractal_function()
    else: data = choose_fractal_from_data()
    print("\nPlease wait now. Your fractal will be assembled.")
    return data
    
