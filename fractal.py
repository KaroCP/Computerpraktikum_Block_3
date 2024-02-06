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

from matplotlib.widgets import Slider
from matplotlib.patches import Rectangle
import colorsys
import time

from newton import newton_approximation


# In[2]

class Fractal:
    """
    Class of an interative Interface which plots a fractal.

    Attributes
    ----------
    fig : matplotlib.figure.Figure
        Figure form the interface.
    func : function
        Function from C to C, which will be used to generate the fractal.
    diff : function
        The derivative of func. 
    label : str
        The mapping rule of func or some other symbol for it.
    max_iterations : int
        The number if the maximal iterations in the newton approximation.
        The default is 128.
    tolerance : float
        The tolerance in the newton approximation.
        The default is 10e-7.
    density : int
        number of pixel in each row and each colum.
        The default is 64.
    start_lims : np.ndarray of form [[x_min, y_min], [x_max, y_max]]
        Contains the information, in which area in the compley plane 
        the first plot will be generated.
        The default is [[-1, -1], [1, 1]].
    start_time : float
        The value when the program is started to calculate later,
        how long the program is still running.
    pointer : np.ndarray of shape (2,) or None
        If not None it gives the point at which the automatic zoom will focus.
        The default is None.
    roots : np.ndarray of shape (n+1,)
        Array of the n calculated complex roots of func.
        With Inf as additional entry for divergence.
    colors : np.ndarray of floats with shape (n+1,)
        Array of the hue value of colors. For each root one color.
    lims : list
        All Elements has to have the form [[x_min, y_min],[x_max, y_max]].
        Contains all previous limits as information for zooming backwards.
        The last entry contains the current limits.
    plot_data : array of shape (density, density, 3)
        Contains the plot data so it has not to be recalculated each time.
    zoom : bool
        If True the user can zoom by drawing a rectangle.
        If False the user can zoom with the mousewheel and shift the plot with
        drag and drop. Only reasonable if the calculation is fast.
        The default is True.
    rectangle : matplotlib.patches.Rectangle or None
        If not None, the rectangle which is drawn to zoom for the first zoom
        option.
    text : bool
        If True an infobox is plotted above the fractal.
        The default is False.
    calulation_time : float
        Calculation time of the last calculation for plot data.
    slider : matplotlib.widgets.Slider
        The slider on the plot for shanging the pixel density.

    Methods
    -------
    set_roots(roots)
        Replaces roots and colors with new roots and respective colors.
    set_lims(lims)
        Adds lims to the list of all previous limits.
    get_info_str()
        Returns a string containig the information for the infobox.
    slider_update(value)
        The update function for the slider.
    update(recalculate=True)
        Method to update the plot with new settings.
        If rerecalculate is True the plot data will be recalculated.
        Otherwise tho old plot data will be used.
    color_newton()
        Calculates for each point in the grid depending on the limits and the 
        density the resulting color by using the in python coded newton
        approximation.
    switch_zoom(event)
        Individual functions with respective queries for specific inputs for 
        interaction with the keyboard.        
    zoom1(event)
        First and standard zoom option. Zoom by drawing a rectangle.
    zoom2(event)
        Second method for zooming. 
        Zoom with the mouse wheel in and out of the plot.
    translation(event)
        Method for drag and drop. 
        Only possible when using the second zoom option and fast calculation.
    isVisible()
        Tests wether the figure is stil open (-> True) 
        or was closed (-> False).
    kino()
        Function for the animated zoom. If there is a pointer the plot will 
        be zoomed in automaticly.
    """

    def __init__(self, func, diff=None, label=None, pointer=None,
                 density=64, max_iteration=128, tolerance=10e-7):
        """
        Parameters
        ----------
        Init parameters for the fractal.
        Have to have the same type and desctiption als their class attribute.
        """
        # Consatants:
        self.fig = plt.figure()  # This creates canvas
        self.fig.subplots(1)
        self.fig.subplots_adjust(left=0.15)  # make space for the slider

        self.func = func
        self.diff = diff
        self.label = label

        self.max_iteration = max_iteration
        self.tolerance = tolerance
        self.density = density

        self.start_lims = np.array([[-1, -1], [1, 1]])
        self.start_time = time.perf_counter()
        self.pointer = pointer

        # Variables:
        self.set_roots()
        self.set_lims()
        self.plot_data = np.zeros((self.density, self.density, 3))

        self.zoom = True
        self.fig.canvas.mpl_connect('key_press_event', self.switch_zoom)
        self.bindingidtranslation = None
        self.bindingidbuttonrelease = None
        self.bindingidzoom = self.fig.canvas.mpl_connect('button_press_event',
                                                         self.zoom1)
        self.rectangle = None
        self.text = False

        self.update(True)


# In[3]


    def set_roots(self, roots=None):
        """
        Replaces roots and colors with new roots and respective colors.

        Parameters
        ----------
        roots : array-like of shape (n+1), optional
            New calculated roots of func with Inf as additional entry for 
            divergence.            
            The default is None.
        """
        if np.any(roots == None):
            self.roots = None
            self.colors = None
        else:
            self.roots = np.array(roots)
            self.colors = np.linspace(0, 1, len(self.roots))

    def set_lims(self, lims=None):
        """
        Adds lims to the list of all previous limits.

        Parameters
        ----------
        lims : array-like of form [[x_min, y_min],[x_max, y_max]], optional
            If not None lims will be added to self.lims and therefore become
            the new limits. 
            Otherwise the zoom will be reseted th the initial limits.
            The default is None.
        """
        if np.any(lims == None):
            self.lims = [self.start_lims]
        else:
            self.lims.append(np.array(lims))

    def get_info_str(self):
        """
        Returns a string containing the information for the infobox.
        It concludes:
            self.label i.e. the mapping rule of self.func
            The number of pixels
            The number of different calculated roots.
            The complex roots with their respective color hue.

        Returns
        -------
        str
            Infostring about the function and the plot.
        """
        textstr1 = '\n'.join(("The function is "+self.label,
                              "and the fractal is ploted with {}*{} pixels.".format(
                                  self.density, self.density),
                              "The {} roots with resp. color in hsl are:".format(
                                  len(self.roots)-1), ""))
        textstr2 = '\n'.join([str(self.roots[i])+", " +
                              str(int(255*self.colors[i]))
                              for i in range(len(self.roots)-1)])
        return textstr1+textstr2

    def slider_update(self, val):
        """
        The update function for the slider.

        Parameters
        ----------
        val : numpy.float64
            Contains the information of the slider value.
        """
        self.density = int(np.power(10, val))
        self.update(True)


# In[4]

    def update(self, recalculate=False):
        """
        Method to update the plot with a new grid.

        If recalculate is True new plot data will be calculated. 
            Otherwise the old plot data will be used.
        If self.text is True a Infobox will be printed on the plot.
        If one is zooming with zoom option 1 a rectangle will be drawn.
        At the left side a slider for the density will be drawn.
        """
        self.fig.clf()  # Clear canvas
        ax = self.fig.add_subplot()  # create new subplot

        # renew plots
        if recalculate:
            start_time = time.perf_counter()
            self.plot_data = self.color_newton()
            self.calulation_time = time.perf_counter()-start_time
        # Set origin to habe no inverted y-axis.
        # Give extend to have realistic subscription at the axis.
        ax.imshow(self.plot_data, origin="lower",
                  extent=self.lims[-1].T.flatten())
        if self.text:
            to_text = plt.figtext(0.5, 0.95, self.get_info_str(), fontsize=6,
                                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))
            to_text.set_horizontalalignment("center")
            to_text.set_verticalalignment("top")
        if self.rectangle != None:
            ax.add_patch(self.rectangle)

        # Init Slider
        slider_ax = self.fig.add_axes([0.08, 0.1, 0.02, 0.79])
        self.slider = Slider(ax=slider_ax,
                             label="Pixel densit\nin log scale", valmin=0.5, valmax=3.5,
                             valinit=np.log10(self.density), orientation="vertical")
        self.slider.on_changed(self.slider_update)

        # draw
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


# In[5]


    def color_newton(self):
        """
        Calculates the fractal structure on the grid.        

        Returns
        -------
        np.ndarray of shape (self.density,self.density,3)
            The plot data depending on the current settings.
        """
        grid = np.meshgrid(np.linspace(*self.lims[-1][:, 0], self.density),
                           np.linspace(*self.lims[-1][:, 1], self.density))
        roots, root_hue, iter_light = newton_approximation(self.func,
                                                           self.diff, grid, self.max_iteration, self.tolerance)
        self.set_roots(roots)
        iter_light = np.array((7/8*iter_light/self.max_iteration+1/8))
        iter_light[root_hue == len(self.roots)-1] = 1
        root_hue = self.colors[root_hue.astype(int)]

        return np.array(np.vectorize(colorsys.hls_to_rgb)(
                        root_hue, iter_light, 1)).transpose(1, 2, 0)


# In[6]

    def switch_zoom(self, event):
        """
        Method to interact with the keyboard.
        The programme queries in individual if loops whether certain keys are 
        pressed and, if so, executes the corresponding operation.

        'z' is pressed: Switch bewteen the two zoom options.
        'b' is pressed: Zoom back to the last zoom.
        'o' is pressed: Zoom out the fix property of 2.
        'r' is pressed: Reset the zoom to the first limits.
        't' is pressed: Toggle the infobox.

        Parameters
        ----------
        event : matplotlib.backend_bases.KeyEvent
            Object which contains the information about the pressd keyboard 
            key.
        """
        if event.key == "z":  # switch between the two zoom options
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
        elif event.key == "b":  # Zoom to the last zoom
            if len(self.lims) == 1:
                print("No zoom state before initial state.")
            else:
                self.lims.pop(-1)
                self.update(True)
        elif event.key == "o":  # Zoom out
            center = np.sum(self.lims[-1], axis=0)/2
            self.set_lims(2*(self.lims[-1]-center)+center)
            self.update(True)
        elif event.key == "r":  # reset
            self.set_lims()
            self.update(True)
        elif event.key == "t":  # Toggle infobox
            self.text = not self.text
            self.update()


# In[7]

    def zoom1(self, event):
        """
        Method for zooming by drawing a rectangle.

        Parameters
        ----------
        event : matplotlib.backend_bases.PickEvent
            Object which contains the information of the coordinates of 
            the mouse pointer.
        """
        val1 = np.array([event.xdata, event.ydata])

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
            val2 = np.array([event_2.xdata, event_2.ydata])
            if np.array(val2 != None).all():
                self.rectangle = Rectangle(val1, *(val2-val1),
                                           color=(0.5, 0.5, 0.5, 0.7))
                self.update()
        moving_id = self.fig.canvas.mpl_connect(
            'motion_notify_event', motion_notify)

        def button_release(event_3):
            """
            Ends the drag-and-drop action.

            Parameters
            ----------
            event_3 : matplotlib.backend_bases.MouseEvent
                Object which contains the information of the coordinates of 
                the mouse pointer.
            """
            plt.disconnect(moving_id)
            plt.disconnect(self.bindingidbuttonrelease)
            self.bindingidbuttonrelease = None
            self.rectangle = None

            val2 = np.array([event_3.xdata, event_3.ydata])
            if None not in np.array([val1, val2]) and not (val1-val2 == 0).any():
                self.set_lims(np.sort([val1, val2], axis=0))
                self.update(True)
            else:
                self.update()
        self.bindingidbuttonrelease = self.fig.canvas.mpl_connect(
            'button_release_event', button_release)


# In[8]

    def zoom2(self, event):
        """
        Module to zoom in and out of the plot.

        Parameters
        ----------
        event : matplotlib.backend_bases.MouseEvent
            Object that contains the information about how far scrolling has 
            taken place.
        """
        position = np.array([event.xdata, event.ydata])
        if np.any(position == None):
            position = np.sum(self.lims[-1], axis=0)/2
        self.set_lims((1-0.05*event.step)*(self.lims[-1]-position)+position)
        self.update(True)

    def translation(self, event):
        """
        Method for shofting the plot by drag and drop.

        Parameters
        ----------
        event : matplotlib.backend_bases.PickEvent
            Object which contains the information of the coordinates of 
            the mouse pointer.
        """
        value1 = np.array([event.xdata, event.ydata])
        self.set_lims(self.lims[-1])

        def motion_notify(event_2):
            """
            Function for translation to plot in the new limits.

            Parameters
            ----------
            event_2 : matplotlib.backend_bases.MouseEvent
                Object which contains the information of the coordinates of 
                the mouse pointer.
            """
            value2 = np.array([event_2.xdata, event_2.ydata])
            if np.array(value2 != None).all():
                self.lims[-1] = self.lims[-1] + value1-value2
                self.update(True)

        moving_id = self.fig.canvas.mpl_connect(
            'motion_notify_event', motion_notify)

        def button_release(event_3):
            """
            Ends the drag-and-drop action.

            Parameters
            ----------
            event_3 : matplotlib.backend_bases.MouseEvent
                Standard variable for functions with mpl_conect. 
                Not needed in this case.
            """
            plt.disconnect(moving_id)
            plt.disconnect(self.bindingidbuttonrelease)
            self.bindingidbuttonrelease = None
        self.bindingidbuttonrelease = self.fig.canvas.mpl_connect(
            'button_release_event', button_release)


# In[9]

    def isVisible(self):
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
        """
        Function for the animated zoom. If there is a pointer the plot will 
        be zoomed in automaticly.
        """
        if self.pointer != None:
            self.set_lims(np.exp(-0.06*(time.perf_counter()-self.start_time))*(self.start_lims
                                                                       - self.pointer)+self.pointer)
            self.update(True)
