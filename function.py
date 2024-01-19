'''
Definition of the class Fractal
That contains data like the function, which is used to construct the fractal, 
    or the maximum iteration level. And it and defines functions to create 
    (and update?) the plot.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
import matplotlib.pyplot as plt

import colorsys

# from sympy.utilities.lambdify import implemented_function
# from sympy.abc import x
# from sympy import diff
# from sympy import lambdify
# from sympy import roots
# from sympy import solve

from newton import newton_approx


# In[2]

class Fractal: 
    #TODO inplement symbolic calculation of derivative and roots.
    
    def __init__(self,func,f_diff=None,zeroset=None,max_iter=200,tol=10e-7,dens=50):
        """
        Parameters
        ----------
        func : 1D array with shape (2,2)
            With functions as entries.
            [f1(x1,x2)
             f2(x1,x2)].
        f_diff : 2D array with shape (2,2), optional
            With functions as entries. The default is None.
            [df1/dx1 df1/dx1
             df2/dx1 df2/dx2]
        zeroset : array-like with shape (n,2) with n arbitrary natural number
            The set of roots from f in form of [real part, imaginary part]
        max_iterations : int
            The number if the maximal iterations in the newton approximation.
            The default is 200.
        tolerance : float
            The tolerance in the newton approximation. The default is 0.01.
        density : int
            number of pixel in each row and colum.
        """
        self.func = lambda a,b:[np.real(func(a+b*1J)), np.imag(func(a+b*1J))] #TODO
        # self.func = func
        if f_diff == None: self.diff = self.calculate_diff(self.func)
        else: self.diff = f_diff
        if zeroset == None: self.roots = self.calculate_zeroset(self.func)
        else: self.roots = np.append(zeroset,[[np.Inf,np.Inf]], axis=0)
        
        self.max_iteration = max_iter
        self.tolerance = tol
        self.density = dens
        
        self.colors = np.linspace(0,1,len(self.roots))
        self.fig, self.ax = plt.subplots()
        self.grid_template = np.array(np.meshgrid(np.linspace(-1,1,self.density),
                            np.linspace(-1,1,self.density))).transpose(1,2,0)
        
    
# In[3]
    
    def color_newton(self,zoom=1, translation=[0,0]):
        """
        Plots the fractal structure on a grid.
    
        Parameters
        ----------
        f : Function
            Says from which function the structure is plotted.
        zoom : float, optional
            Variable to measure the zoom. The default is 1.
        translation : (2,) array of floats, optional
            Variable to measure the translation. The default is 0.
        """
        h = np.vectorize(colorsys.hsv_to_rgb)
        newton = np.vectorize(lambda px, py: newton_approx(self.func,self.diff,
                    [px,py],self.roots[:-1],self.max_iteration,self.tolerance))
        points = zoom*(self.grid_template+translation)
        
        root_hue, iter_light = np.array(newton(points[:,:,0],points[:,:,1]))
        iter_light = np.array((1/2*iter_light/self.max_iteration+3/8))
        root_hue = self.colors[root_hue.astype(int)]
        mask = np.kron(root_hue==1,np.ones(3)).reshape((self.density,
                                                self.density,3)).astype(bool)

        color = np.array(h(root_hue,1,iter_light)).transpose(1,2,0)
        color[mask]=1
        self.im = self.ax.imshow(color)
        # return self.im
        
    
# In[4]
    
    def calculate_diff(self): #TODO
        """
        Returns
        -------
        f_diff : function
            At each point (a,b) it is the Jacobi matrix of self.func
        """
        # f_here = implemented_function('g', lambda x:f(x))
        # f_diff = diff(f_here(x),x)
        # f_diff = lambdify(x, f_diff(x))
        # return lambda x:x+1
        pass
        
    
# In[5]
    
    def calculate_zeroset(self): #TODO
        """
        Returns
        -------
        zeroset : np.ndarray with shape (n,2)
            The set roots of self.func. There are n roots of self.func.
        """
        # g = implemented_function('g', lambda x:f(x))
        # zeroset = solve(g(x)==0,x)
        # zeroset = roots(g(x),x)
        # return zeroset + [np.Inf]
        pass
    