#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np


# In[2]

tolerance = 0.1
max_iteration = 128


# In[10]

#LoremIpsumDolorSitAmet
def newton_approx(f, f_diff, zeroset, point): #TODO import zeroset and f´?
    """
    Placeholder for the Newton approximation.

    Parameters
    ----------
    f : function
        Function from C to C from which the root will be calculated.
    point : array-like
        Startpoint of the Newton approximation. Has to have shape (2,).

    Returns
    -------
    root : int
        The index of the root, which is approximated, in zeroset.
    iteration_level : int
        Number of iterations until the recursion terminates.

    """
    iteration_level = np.sum(point) # nonsence
    root = np.min(point)#len(np.array(point))
    return root, iteration_level

