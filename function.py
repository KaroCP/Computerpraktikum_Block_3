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

from matplotlib.patches import Rectangle
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
    # TODO insert documentary
    # TODO inplement symbolic calculation of derivative and roots.
    # TODO implementieren automatic zoom.
    
    def __init__(self,func,f_diff=None,zeroset=None,label=None,dens=50,max_iter=200,tol=10e-7):
        """
        Parameters
        ----------
        func : function
            Function from C to C which will be used to create the fractal.
            Not anymore: 1D array with shape (2,2). In fact: func= [f1(x1,x2), f2(x1,x2)].
        f_diff : 2D array with shape (2,2), optional
            With functions as entries. The default is None.
            [df1/dx1 df1/dx1
             df2/dx1 df2/dx2]
        zeroset : array-like with shape (n,2) with n arbitrary natural number
            The set of roots from f in form of [real part, imaginary part]
        label : str, optional
            The mapping rule of f or some other symbol for it.
        dens : int
            number of pixel in each row and colum.
        max_iter : int
            The number if the maximal iterations in the newton approximation.
            The default is 200.
        tol : float
            The tolerance in the newton approximation. The default is 0.01.
        """
        
        # Consatants:
        self.func = lambda a,b:[np.real(func(a+b*1J)), np.imag(func(a+b*1J))]
        if f_diff == None: self.diff = self.calculate_diff()
        else: self.diff = lambda a,b:[[np.real(f_diff(a+b*1J)), np.real(f_diff(a+b*1J)*1J)],
                                      [np.imag(f_diff(a+b*1J)), np.imag(f_diff(a+b*1J)*1J)]]
        if zeroset == None: self.roots = self.calculate_zeroset()
        else: self.roots = np.append(zeroset,[[np.Inf,np.Inf]], axis=0)
        self.label = label
        
        self.max_iteration = max_iter
        self.tolerance = tol
        self.density = dens
        
        self.colors = np.linspace(0,1,len(self.roots))
        self.fig = plt.figure() # This creates canvas
        self.fig.subplots(1)
        
        
        # Variables:
        self.lims = np.array([[-1,1],[-1,1]]) # has form [[x_min, x_max],[y_min, y_max]]
        self.plot = np.zeros((self.density,self.density,3))
        
        self.zoom = True        
        self.fig.canvas.mpl_connect('key_press_event', self.switch_zoom)
        self.bindingidtranslation = None
        self.bindingidbuttonrelease = None
        self.bindingidzoom = self.fig.canvas.mpl_connect('button_press_event', self.zoom1)
        self.rectangle = None
        self.recalculate = True
        
        
        self.update()
        
    
# In[3]
    
    def calculate_diff(self):
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
        raise NotImplementedError("The symbolic calculation of the derivative",
                                  "has not yet been implemented.")
        
    
    def calculate_zeroset(self):
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
        raise NotImplementedError("The symbolic calculation of the roots",
                                  "has not yet been implemented.")
        
    
# In[4]
    
    def update(self):
        """
        Method to update the plot with a new grid.
        """
        self.fig.clf() # Clear canvas
        ax = self.fig.add_subplot() # create new subplot
        ax.set_title(self.label)
        
        # renew plots
        if self.recalculate: 
            grid = np.array(np.meshgrid(np.linspace(*self.lims[0],self.density),
                            np.linspace(*self.lims[1],self.density)))
            self.color_newton(grid)
            self.recalculate = False
        else: ax.imshow(self.plot)
        if self.rectangle != None: ax.add_patch(self.rectangle)
        
        # draw
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    
# In[5]
    
    def color_newton(self, grid):
        """
        Calculates and plots the fractal structure on the grid.
        """
        h = np.vectorize(colorsys.hsv_to_rgb)
        newton = np.vectorize(lambda px, py: newton_approx(self.func,self.diff,
                    [px,py],self.roots[:-1],self.max_iteration,self.tolerance))
        
        root_hue, iter_light = np.array(newton(*grid))
        iter_light = np.array((1/2*iter_light/self.max_iteration+3/8))
        root_hue = self.colors[root_hue.astype(int)]

        self.plot = np.array(h(root_hue,1,iter_light)).transpose(1,2,0)
        self.plot[root_hue==1]=1
        return plt.imshow(self.plot)
        
    
# In[6]
    
    def switch_zoom(self,event):
        if event.key == "z": # switch between the two zoom options
            self.zoom = not self.zoom
            if self.zoom:
                plt.disconnect(self.bindingidtranslation)
                plt.disconnect(self.bindingidzoom)
                self.bindingidtranslation = None
                self.bindingidzoom = self.fig.canvas.mpl_connect('button_press_event', self.zoom1)
            else:
                plt.disconnect(self.bindingidzoom)
                self.bindingidzoom = self.fig.canvas.mpl_connect('scroll_event', self.zoom2)
                self.bindingidtranslation = self.fig.canvas.mpl_connect('button_press_event', self.translation)
        if event.key == "r": #reset
            self.lims = np.array([[-1,1],[-1,1]])
            self.recalculate = True
            self.update()
        if event.key == "o": #Zoom out
            self.lims = 10*self.lims
            self.recalculate = True
            self.update()
        
    
# In[7]
    
    def zoom1(self,event):
        value1 = np.array([event.xdata, event.ydata])
        def motion_notify(event_2):
            """
            Function for zoom to animate the position of the mouse 
            pointer and the resulting image.
    
            Parameters
            ----------
            event_2 : matplotlib.backend_bases.MouseEvent
                Object which contains the information of the coordinates of 
                the mouse pointer.
            """
            value2 = np.array([event_2.xdata, event_2.ydata])
            if np.array(value2 != None).all():
                self.rectangle = Rectangle(value1, *(value2-value1),color=(0.5,0.5,0.5,0.7))
                self.update()
        moving_id = self.fig.canvas.mpl_connect('motion_notify_event', motion_notify)
            
        def button_release(event_3):
            plt.disconnect(moving_id)
            plt.disconnect(self.bindingidbuttonrelease)
            self.bindingidbuttonrelease = None
            self.rectangle = None
            value2 = np.array([event_3.xdata, event_3.ydata])
            if None not in np.array([value1,value2]) and not (value1-value2==0).any():
                self.lims = (np.multiply((self.lims[:,1]-self.lims[:,0])/self.density,
                             np.sort([value1, value2], axis=0))+self.lims[:,0]).T
                self.recalculate = True
                self.update() 
            else: self.update()
        self.bindingidbuttonrelease = self.fig.canvas.mpl_connect('button_release_event', button_release)
        
    
# In[8]
    
    def zoom2(self,event):
        # old_lim = self.lims.T-(self.lims[:,1]+self.lims[:,0])/2 #TODO
        # self.lims = (old_lim*(1-0.05*event.step)+[event.xdata,event.ydata]).T        
        self.lims = self.lims*(1-0.05*event.step)
        self.recalculate = True
        self.update()
        
    
    def translation(self,event):
        pass #TODO implement "drag_and_drop" from plotstuff
        
    
# In[9]
    
    
