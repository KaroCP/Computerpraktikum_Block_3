#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np

from sympy.utilities.lambdify import implemented_function
from sympy.abc import x
from sympy import diff
from sympy import lambdify
from sympy import roots
from sympy import solve

from newton import newton_approx #outsorcing of the definition


# In[2]

class Function: # funktioniert bis jetzt nur, wenn man auch Ableitung und Nullstellenmenge eingibt.
    
    def __init__(self,input_function, f_diff=None):
        """
        Parameters
        ----------
        input_function : TYPE
            DESCRIPTION.
        f_diff : 2D array with shape (2,2), optional
            With functions as entries. The default is None.
            [df/dx df/dy
                ]

        Returns
        -------
        None.

        """
        self.f = np.vectorize(lambda x:input_function(x))
        if f_diff == None: self.diff = calculate_diff(self.f)
        else: self.diff = np.vectorize(lambda x:f_diff(x))
        self.newton = np.vectorize(lambda px,py: newton_approx(self.f,self.diff))#,self.roots,[px,py]))
    
    
# In[3]

    
    def initialize_root(self,zeroset=None):
        if zeroset == None: self.roots = calculate_zeroset(self.f)
        else: self.roots = np.append(np.array(zeroset),np.Inf)
        self.colors = np.append(define_colors(self.roots[:-1]),1000)
     
        

# In[3]


def calculate_diff(f): #TODO
    """
    Parameters
    ----------
    f : function
        The function whose derivative will be calculated.

    Returns
    -------
    f_diff : function
        Derivative of f.
    """
    f_here = implemented_function('g', lambda x:f(x))
    # f_diff = diff(f_here(x),x)
    # f_diff = lambdify(x, f_diff(x))
    return lambda x:x+1


# In[3]

def calculate_zeroset(f): #TODO
    """
    Parameters
    ----------
    f : function
        The function whose roots will be calculated.

    Returns
    -------
    zeroset : 1D array of floats
        The roots of f with infinity as additional last entry.

    """
    g = implemented_function('g', lambda x:f(x))
    zeroset = solve(g(x)==0,x)
    # zeroset = roots(g(x),x)
    return zeroset + [np.Inf]


# In[4]

def define_colors(zeroset):
    return np.linspace(0,1,len(zeroset))


# In[100]

from sympy import sin

f = lambda x: x+1
# f_diff = calculate_zeroset(f)
# print(f_diff)
pre = [1,2,3]
# print(define_colors(pre))
