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
from matplotlib.widgets import Slider as Slid


# In[2]

class Slider: #TODO everything
    
    def __init__(self,update,update_func_only_on_release_event=False, **kwargs):
        """
        

        Parameters
        ----------
        update : TYPE
            DESCRIPTION.
        update_func_only_on_release_event : TYPE, optional
            DESCRIPTION. The default is False.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.slid = Slid(**kwargs)
        
    
# In[3]
    
    def calculate_diff(self):
        pass