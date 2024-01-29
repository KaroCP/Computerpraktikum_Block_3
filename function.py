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
import subprocess
import time

# from sympy.utilities.lambdify import implemented_function
# from sympy.abc import x
# from sympy import diff
# from sympy import lambdify

old = False
if old: 
    new = False
    from newton_works import newton_approx,newton_with_matrices,newton #TODO
else:   
    polynom_degre = 3 #TODO
    from newton_von_Valentino_hoffentlich_richtig import newton_approx_with_grid,sort_roots


# In[2]

class Fractal:
    """
    Class of an interative Interface which plots a fractal.
    
    Attributes
    ----------
    fig : matplotlib.figure.Figure
        Figure form the interface.
    func : function in two variables
        The function which generates the fractal. 
    diff : function in two variables
        At each point the Jacobian of func. 
    roots : np.ndarray
        Array of the roots of func written as 2-dimensional data points.
        With [Inf,Inf] as additional entry for divergence.
    colors : np.ndarray
        Array colors. for each root one color.
    label : str
        Name or maping rule of func.
    density : int
        number of pixel in each row and colum.
    max_iterations : int
        The number if the maximal iterations in the newton approximation.
        The default is 200.
    tolerance : float
        The tolerance in the newton approximation. The default is 0.01.
    fast : bool, optional
        Says which calculation will be used. 
        The faster calculation with C++ or the slower one in python.
        The default is True.
    lims : array of form [[x_min, y_min],[x_max, y_max]]
        Contains the information, in which area in the compley plane 
        the function is plotted.
    plot_data : array with shape (density,density,3)
        Contains the color data at each point so it has not to be 
        recalculated each time

    Methods
    -------
    calculate_diff()
        Calculates the derivative of func symbolc
    calculate_zeroset()
        Calculates the derivative of func symbolc
    update()
        Method to update the plot with limits.
    color_newton(grid)
        Calculates at each point the resulting color 
        by using the newton approximation.
    switch_zoom(event)
        Individual functions with respective queries for specific inputs for 
        interaction with the keyboard.        
    zoom1(event)
        First and standard zoom option. Zoom by drawing a rectangle.
    zoom2(event)
        Second method for zooming. 
        Zoom with dhe mouse wheel in and out of the plot.
    translation(event)
        Method for drag and drop. 
        Only possible when using the second zoom option and fast calculation.
    isVisible()
        Tests wether the figure is stil open (-> True) 
        or was closed (-> False).
    kino()
        Placeholder for animated zoom. #TODO
    """
    # TODO inplement symbolic calculation of derivative.
    
    def __init__(self,func,f_diff=None,zeroset=None,label=None,
                 dens=50,max_iter=20,tol=10e-7, fast=True,pointer=None):
        """
        Parameters
        ----------
        func : function
            Function from C to C which will be used to create the fractal.
            Not anymore: 1D array with shape (2,2). 
            In fact: func= [f1(x1,x2), f2(x1,x2)].
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
        fast : bool, optional
            Says which calculation will be used. 
            The faster calculation with C++ or the slower one in python.
            The default is True.
        pointer : arry of form [x,y].
            For the animated zoom. at which direction the zoom will be.
            Still a bit #TODO!
        """
        
        # Consatants:
        self.func = lambda a,b:[np.real(func(a+b*1J)), np.imag(func(a+b*1J))]
        if f_diff == None: f_diff = self.calculate_diff()
        self.diff = lambda a,b:[[np.real(f_diff(a+b*1J)), 
                                 np.real(f_diff(a+b*1J)*1J)],
                                [np.imag(f_diff(a+b*1J)), 
                                 np.imag(f_diff(a+b*1J)*1J)]]
        if np.any(zeroset == None): zeroset = None
        self.label = label
        if old: 
            if new:
                self.func = np.vectorize(func)
                self.diff = np.vectorize(f_diff)
            else: self.set_roots(np.append(zeroset,[[np.Inf,np.Inf]], axis=0))
        else: self.set_roots(None)
        
        self.max_iteration = max_iter
        self.tolerance = tol
        self.density = dens
        self.fast = False#fast
        
        self.fig = plt.figure() # This creates canvas
        self.fig.subplots(1)
        
        if pointer != None: 
            self.pointer = pointer
            self.start_time = time.perf_counter()
        
        
        # Variables:
        self.lims = np.array([[[-1,-1],[1,1]]])
        self.plot_data = np.zeros((self.density,self.density,3))
        
        self.zoom = True        
        self.fig.canvas.mpl_connect('key_press_event', self.switch_zoom)
        self.bindingidtranslation = None
        self.bindingidbuttonrelease = None
        self.bindingidzoom = self.fig.canvas.mpl_connect('button_press_event', 
                                                         self.zoom1)
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
        # x = sympy.symbols('x')
        # func = lambda x:func(x)
        # try: diff = sympy.lambdify(x,func(x).diff(x))
        
        # f_here = implemented_function('g', lambda x:f(x))
        # f_diff = diff(f_here(x),x)
        # f_diff = lambdify(x, f_diff(x))
        raise NotImplementedError("The symbolic calculation of the derivative",
                                  "has not yet been implemented.")
        # except Exception as e: 
        #     raise Exception(e,
        #         "The derivation could not be calculated symbolically.")
    
    
    def set_roots(self,roots):
        if np.any(roots==None): 
            self.roots = None
            self.colors = None #self.roots, and self.color are defined #TODO
        else:
            self.roots = np.array(roots)
            self.colors = np.linspace(0,1,len(self.roots))
        
    
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
            grid = np.meshgrid(np.linspace(*self.lims[-1,:,0],self.density),
                               np.linspace(*self.lims[-1,:,1],self.density))
            if old:
                if new: grid = grid[0]+1J*grid[1]
            if self.fast: #TODO
                self.plot_data = subprocess.run(["/newton_c++.exe", "KARO's INPUT"]) 
            else: self.plot_data = self.color_newton(grid)
            self.recalculate = False
        # set origin to habe not inverst y-axis.
        # Give extend to have realistic subscription at the axis.
        ax.imshow(self.plot_data, origin="lower", extent = self.lims[-1].T.flatten())
        if self.rectangle != None: ax.add_patch(self.rectangle)
        
        # draw
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        
    
# In[5]
    
    def color_newton(self, grid):
        """
        Calculates and plots the fractal structure on the grid.
        """
        h = np.vectorize(colorsys.hls_to_rgb)
        if old:
            if new:
                root_hue, iter_light, roots = newton(self.func, 
                            self.diff, grid, self.max_iteration, self.tolerance)
                # TODO convert complex to real
                self.set_roots(roots)
            else:
                newton = np.vectorize(lambda px, py: newton_approx(self.func,self.diff,
                            [px,py],self.roots[:-1],self.max_iteration,self.tolerance))
                root_hue, iter_light = newton(*grid)
                # root_hue, iter_light, roots = newton_with_matrices(self.func, 
                #             self.diff, grid, self.max_iteration, self.tolerance)
                # self.set_roots(roots)
        else: 
            roots_grid = newton_approx_with_grid(self.func, self.diff, grid, self.max_iteration, self.tolerance)
            value = sort_roots(roots_grid, polynom_degre, self.max_iteration, self.tolerance)
            self.set_roots(value[1])
            root_hue = value[0][:,:,0]
            iter_light = value[0][:,:,2]
        iter_light = np.array((7/8*iter_light/self.max_iteration+1/8))
        root_hue = self.colors[root_hue.astype(int)]

        return np.array(h(root_hue,iter_light,1)).transpose(1,2,0)
        
    
# In[6]
    
    def switch_zoom(self,event):
        if event.key == "z": # switch between the two zoom options
            self.zoom = not self.zoom
            if self.zoom:
                plt.disconnect(self.bindingidtranslation)
                plt.disconnect(self.bindingidzoom)
                self.bindingidtranslation = None
                self.bindingidzoom = self.fig.canvas.mpl_connect(
                                  'button_press_event', self.zoom1)
            else:
                plt.disconnect(self.bindingidzoom)
                self.bindingidzoom = self.fig.canvas.mpl_connect(
                                        'scroll_event', self.zoom2)
                self.bindingidtranslation = self.fig.canvas.mpl_connect(
                                   'button_press_event', self.translation)
        elif event.key == "r": #reset
            self.lims = np.array([[[-1,-1],[1,1]]])
            self.recalculate = True
            self.update()
        elif event.key == "o": #Zoom out
            center = np.sum(self.lims[-1],axis=0)/2
            self.lims = np.append(self.lims,[2*(self.lims[-1]-center)+center],axis=0)
            self.recalculate = True
            self.update()
        elif event.key == "b":
            if len(self.lims)==1:
                print("No zoom state before initial state.")
            else:
                self.lims = np.delete(self.lims,-1,axis=0)
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
                self.rectangle = Rectangle(value1,*(value2-value1),
                                           color=(0.5,0.5,0.5,0.7))
                self.update()
        moving_id = self.fig.canvas.mpl_connect(
             'motion_notify_event', motion_notify)
            
        def button_release(event_3):
            plt.disconnect(moving_id)
            plt.disconnect(self.bindingidbuttonrelease)
            self.bindingidbuttonrelease = None
            self.rectangle = None
            
            value2 = np.array([event_3.xdata, event_3.ydata])
            if None not in np.array([value1,value2]) and not (value1-value2==0).any():
                self.lims = np.append(self.lims,[np.sort([value1, value2], axis=0)],axis=0)
                self.recalculate = True
                self.update() 
            else: self.update()
        self.bindingidbuttonrelease = self.fig.canvas.mpl_connect(
                             'button_release_event', button_release)
        
    
# In[8]
    
    def zoom2(self,event):
        position = np.array([event.xdata,event.ydata])
        if np.any(position==None): position = np.sum(self.lims[-1],axis=0)/2
        self.lims = np.append(self.lims,
                [(1-0.05*event.step)*(self.lims[-1]-position)+position], axis=0)
        self.recalculate = True
        self.update()
        
    
    def translation(self,event):
        value1 = np.array([event.xdata, event.ydata])
        self.lims = np.append(self.lims,[self.lims[-1]],axis=0)
        
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
                self.lims[-1] = self.lims[-1] + value1-value2
                self.recalculate = True
                self.update()
        
        moving_id = self.fig.canvas.mpl_connect(
             'motion_notify_event', motion_notify)
        
        def button_release(event_3):
            plt.disconnect(moving_id)
            plt.disconnect(self.bindingidbuttonrelease)
            self.bindingidbuttonrelease = None
        self.bindingidbuttonrelease = self.fig.canvas.mpl_connect(
                             'button_release_event', button_release)
        
    
# In[9]
    
    def isVisible(self): #for animation. still TODO
        """
        Tests wether the figure is stil open (-> True) 
        or was closed (-> False).

        Returns
        -------
        still_open : bool
            True, if the figure is still active, False if the figure 
            was closed.
        """
        still_open = self.fig.canvas.isVisible()
        return still_open

    def kino(self):
        pass
    