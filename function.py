#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
import colorsys

# from sympy.utilities.lambdify import implemented_function
# from sympy.abc import x
# from sympy import diff
# from sympy import lambdify
# from sympy import roots
# from sympy import solve

from newton import newton_approx #outsorcing of the definition


# In[2]

class Function: # funktioniert bis jetzt nur, wenn man auch Ableitung und Nullstellenmenge eingibt.
    
    def __init__(self, func, f_diff=None, zeroset=None, max_iteration=200, tolerance=10e-7, density=20):
        """
        Parameters
        ----------
        input_function : 1D array with shape (2,2)
            With functions as entries.
            [f1(x1,x2)
             f2(x1,x2)].
        f_diff : 2D array with shape (2,2), optional
            With functions as entries. The default is None.
            [df1/dx1 df1/dx1
             df2/dx1 df2/dx2]
        max_iterations : int
            The number if the maximal iterations in the newton approximation.
            The default is 200.
        tolerance : float
            The tolerance in the newton approximation. The default is 0.01.
        density : int
            number of pixel in each row and colum.
        """
        # self.f = lambda a,b:[np.real(func(a+b*1J)), np.imag(func(a+b*1J))]
        self.f = func
        if f_diff == None: self.diff = self.calculate_diff(self.f)
        else: self.diff = f_diff #TODO schöner machen
        self.max_iteration = max_iteration
        self.tolerance = tolerance
        self.density = density
        self.grid_template = np.array(np.meshgrid(np.linspace(0,1,self.density),
                            np.linspace(0,1,density))).transpose(1,2,0)
        
        self.initialize_root(zeroset)
    
    
# In[3]

    
    def initialize_root(self,zeroset=None):
        if zeroset == None: self.roots = self.calculate_zeroset(self.f)
        else: self.roots = np.append(np.array(zeroset),np.Inf)
        self.colors = np.append(np.linspace(0,1,len(self.roots[:-1])),1000)
        
    
# In[6]
    
    def color_newton(self,zoom, translation):
        h = np.vectorize(colorsys.hsv_to_rgb)
        newton = np.vectorize(lambda px, py: newton_approx(self.f,self.diff,[px,py],self.roots[:-1],self.max_iteration,self.tolerance))
        points = zoom*self.grid_template+translation
        
        hsv_data = np.array(newton(points[:,:,0],points[:,:,1])).transpose(1,2,0).astype(float)
        print(hsv_data.shape, "1") #TODO
        hsv_data[:,:,0] = self.colors[hsv_data[:,:,0].astype(int)]
        hsv_data[:,:,1] = np.array((hsv_data[:,:,1]/self.max_iteration/2+1/4))
        # print(hsv_data)
        color = np.array(h(hsv_data[:,:,0],1,hsv_data[:,:,1])).T
        print(color.shape, "color") #TODO
        mask = np.kron(np.any(hsv_data==1000, axis=2),np.ones(3)).reshape((self.density,self.density,3)).astype(bool)
        color[mask]=1
        return color


# In[4]


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
        # f_here = implemented_function('g', lambda x:f(x))
        # f_diff = diff(f_here(x),x)
        # f_diff = lambdify(x, f_diff(x))
        # return lambda x:x+1
        pass


# In[5]

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
        # g = implemented_function('g', lambda x:f(x))
        # zeroset = solve(g(x)==0,x)
        # zeroset = roots(g(x),x)
        # return zeroset + [np.Inf]
        pass
