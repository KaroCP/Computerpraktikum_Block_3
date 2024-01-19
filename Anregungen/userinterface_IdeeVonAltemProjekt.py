'''
Module creating a class which creates an interactive plot whrere you 
can interact with the data points and the interpolaten between them 
is calculatet in real-time.
'''

import numpy as np
import matplotlib.pyplot as plt
import interpolation
import helpful_functions
import keyboard
import warnings
warnings.filterwarnings("ignore") # Turn off the unnecessary warnings

ids = {'linear':0, 
       'trigonometric':1, 
       'cubic spline (equidistant)':2,
       'cubic spline (euclidian)':3,
       'points':4,
       'points and text':5,
       'points and coordinates':6,
       'points and interactive':7}

def get_lims(data_points, factor):
    """
    Function to create the boundaries of the plot

    Parameters
    ----------
    data_points : np.ndarray
        Array of 2-dimensional points which should be inside the boundaries.
    factor : float
        Factor indicating by how much greater than the exact Border 
        the limits should be.
    
    Returns
    -------
    lims : np.ndarray
        Array of the boundaries of the plot.
        lims = [[x_min, x_max], [y_min, y_max]]
    """
    
    points_x, points_y = data_points.T
    lims_x = np.array([min(points_x), max(points_x)])
    lims_y = np.array([min(points_y), max(points_y)])
    mean_x = (lims_x[0]+lims_x[1])/2
    mean_y = (lims_y[0]+lims_y[1])/2
    lims = np.array([(lims_x-mean_x) * factor + mean_x,(lims_y-mean_y) * factor + mean_y])

    return lims



class Userinterface():
    """
    Class of an interface with with several possibilities of interation.
    
    ...

    Attributes
    ----------
    fig : matplotlib.figure.Figure
        Figure form the interface.
    data_points : np.ndarray
        Array of 2-dimensional data points.
    factor : float
        Factor for the get_lims function.
    plotargs : list
        Contains the informations about what will be plotted.

    Methods
    -------
    set_data_points(data_points)
        Replaces the data points with new data points.
    isVisible()
        Tests wether the figure is stil open (-> True) or was closed (-> False).
    update()
        Method to update the plot with new points and settings.
    add_point(event)
        Method to add a point to the data points.
        Only works with mouse, touchpad is not enough!
    drag_and_drop(event)
        First part:
            Method to delete a point from the data points.
            Only works with mouse, touchpad is not enough!
        Second part:
            Method for drag and drop.
    keyboard_interaction(event)
        Individual functions with respective queries for specific inputs for 
        interaction with the keyboard.        
    zoom(event)
        Method for zooming in and out of the plot.
    """
    
    
    def __init__(self, data_points = None, plotargs = None):
        """
        Parameters
        ----------
        data_points : array-like, optional
            Array of 2-dimensional data points. The default is None.
        plotargs : list, optional
            Contains the informations about what will be plotted.
            1. Entry : linear interpolation
            2. Entry : trigonometric interpolation
            3. Entry : Cubic spline (equidistant) interpolation
            4. Entry : Cubic spline (euclidian distant improved) interpolation
            5. Entry : show points.
            6. Entry : show the number of each point.
            7. Entry : show coordinates
            8. Entry : interactive plot
            The default is [True,False,False,False,False,False,False].
        """
        
        self.fig = plt.figure() # This creates canvas
        self.fig.subplots(1)
        self.data_points = helpful_functions.check_points(data_points)
        self.factor = 1.3
        self.plotargs = plotargs
        self.bindingidaddpoint = None
        self.bindingidpickevent = None
            
        if self.plotargs == None:
            self.plotargs = [True,False,False,False,False,False,False]
            
        self.fig.canvas.mpl_connect('key_press_event', self.keyboard_interaction)
        self.fig.canvas.mpl_connect('scroll_event', self.zoom)
        self.update()
    
    
    def set_data_points(self, data_points):
        """
        Replaces the data points with new data points.

        Parameters
        ----------
        data_points : np.ndarray
            New array of 2-dimensional data points.
        """
        self.data_points = data_points
        self.update()
        
    def isVisible(self):
        """
        Tests wether the figure is stil open (-> True) or was closed (-> False).

        Returns
        -------
        still_open : bool
            True, if the figure is still active, False if the figure was closed.
        """
        still_open = self.fig.canvas.isVisible()
        return still_open
    
    
    def update(self):
        """
        Method to update the plot with new points and settings.
        """
        self.fig.clf() # Clear canvas
        self.lims = get_lims(self.data_points, self.factor) # set new boundaries
        ax = self.fig.add_subplot(111, xlim=self.lims[0], ylim=self.lims[1]) # create new subplot
        ax.set_aspect('equal')
        
        # Renew plots
        if self.shouldplot('linear'):
            interpolation.linear(self.data_points)
        if self.shouldplot('trigonometric'):
            interpolation.trigonometric(self.data_points)
        if self.shouldplot('points') or self.shouldplot('points and text') or self.shouldplot('points and coordinates') or self.shouldplot('points and interactive'):
            interpolation.show_points(self.data_points, 
                                      text=self.shouldplot('points and text') and len(self.data_points)<200,
                                      coord=self.shouldplot('points and coordinates') and len(self.data_points)<200)
        if self.shouldplot('cubic spline (equidistant)'):
            interpolation.cubic_spline(self.data_points, prop = False)
        if self.shouldplot('cubic spline (euclidian)'):
            interpolation.cubic_spline(self.data_points, prop = True)
        self.fig.legend()
        
        if self.bindingidaddpoint != None and not self.shouldplot('points and interactive'):
            plt.disconnect(self.bindingidaddpoint)
            plt.disconnect(self.bindingidpickevent)
            self.bindingidaddpoint = None
            self.bindingidpickevent = None
        if self.bindingidaddpoint == None and self.shouldplot('points and interactive'):
            self.bindingidaddpoint = self.fig.canvas.mpl_connect('button_press_event', self.add_point)
            self.bindingidpickevent = self.fig.canvas.mpl_connect('pick_event', self.drag_and_drop)
        
        # draw
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
    
    
    def shouldplot(self, methodname):
        """
        Returns true if method should be plotted and false otherwise.

        Parameters
        ----------
        methodname : str
            name of method in ids dictionary

        Returns
        -------
        bool

        """
        return self.plotargs[ids[methodname]]
    
    
    def add_point(self, event):
        """
        Method to add a point to the data points.
        When a position on the point is clicked and "a" is pressed on the 
        keyboard, the coordinates of the position are added to the data 
        points of the interpolation. The point is added to the array of 
        points at the point where the distance is smallest.
        Only works with mouse, touchpad is not enough!
        Only works if the option "interactive plot" has been activated/selected.
        
        Parameters
        ----------
        event : matplotlib.backend_bases.MouseEvent
            Object which contains the information about the coordinates of 
            the location that is clicked on.
        """
        
        if keyboard.is_pressed('a'):
            value = np.array([event.xdata, event.ydata])
            
            if not (None in value):
                norm = np.linalg.norm
                distances = list(map(norm, self.data_points - value))
                pivot_index = np.argmin(distances)
                sucessor_index = pivot_index + 1
                predecessor_index = pivot_index - 1
                
                if pivot_index == 0:
                    predecessor_index = len(self.data_points)-2
                
                pivot = self.data_points[pivot_index]
                suc = self.data_points[sucessor_index]
                pred = self.data_points[predecessor_index]
                
                if (norm(pred-value) + norm(value-pivot))/norm(pred-pivot) < (norm(suc-value) + norm(value-pivot))/norm(suc-pivot):
                    self.data_points = np.insert(self.data_points,predecessor_index + 1, value,axis = 0)
                else:
                    self.data_points = np.insert(self.data_points,pivot_index + 1, value,axis = 0)
            self.update()
    
    
    def drag_and_drop(self, event):
        """
        Method consists of two parts:
            
            First part:
                Method to delete a point from the data points.
                When a data point is picked and "d" is pressed on the 
                keyboard, the point will be deleted from the data points.
                Only works with mouse, touchpad is not enough!
                
            Second part:
                Method for drag and drop.
                When a point is picked, the coordinates of the point are the 
                coordinates of the mouse pointer until the point/button is 
                released.
        Only works if the option "interactive plot" has been activated/selected.

        Parameters
        ----------
        event : matplotlib.backend_bases.PickEvent
            Object which contains the information about the index of the 
            point, that is picked. 
        """
        
        index = event.ind
        
        # Deleting points
        if keyboard.is_pressed('d'): 
            
            if self.data_points.shape[0]==2: 
                print("You can't delete the last point")
            
            else: 
                self.data_points = np.delete(self.data_points, index[0], axis=0)
                if index[0] == 0: self.data_points[-1] = self.data_points[0]
                self.update()
                
            return None
        
        
        # Drag-and-drop
        def motion_notify(event_2):
            """
            Function for drag-and-drop to animate the position of the mouse 
            pointer and the resulting interpolations.

            Parameters
            ----------
            event_2 : matplotlib.backend_bases.MouseEvent
                Object which contains the information of the coordinates of 
                the mouse pointer.
            """
            position = np.array([event_2.xdata, event_2.ydata])
            if np.array(position != None).all(): 
                self.data_points[index] = position
            self.update()
        
        moving_id = self.fig.canvas.mpl_connect('motion_notify_event', motion_notify)
        
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
            
        self.fig.canvas.mpl_connect('button_release_event', button_release)
    
    
    def keyboard_interaction(self, event):
        """
        Method to interact with the keyboard.
        The programme queries in individual if loops whether certain keys are 
        pressed and, if so, executes the corresponding operation.
        
        id of method is pressed: Toggle interpolation method
        'z' is pressed: Print coordinates of the points. Only possible if 
            there are not to many points.
        'i' is pressed: Print Informations about the plot and interact with it.

        Parameters
        ----------
        event : matplotlib.backend_bases.KeyEvent
            Object which contains the information about the pressd keyboard key.
        """
            
        for i in range(1,len(ids)+1):
            if event.key == str(i):
                self.plotargs[i-1] = not self.plotargs[i-1]
                self.update()
        
        if event.key == "z" and len(self.data_points)<=200:
            print("points of form [id, x, y]")
            points_show = np.append([np.array(range(1, self.data_points.shape[0]+1))], self.data_points.T, 0).T
            print(points_show[:-1], "\n")
    
    
    def zoom(self, event):
        """
        Module to zoom in and out of the plot.

        Parameters
        ----------
        event : matplotlib.backend_bases.MouseEvent
            Object that contains the information about how far scrolling has 
            taken place.
        """
        
        self.factor = self.factor*(1-0.05*event.step)
        self.update()
