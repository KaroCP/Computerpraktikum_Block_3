'''
Newton approximation form Karo.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
import time

import warnings
warnings.filterwarnings("ignore")


# In[2]

def catch(func, *args, handle=None):
    try: return func(*args)
    except Exception as e: 
        return handle
    

# In[3]

def newton_approximation(func, diff, grid, max_iterations, border):
    """
    Newton approximation of roots for complex functions.
    Calculating the resluts simultanuously by using matrixmultiplication.

    Parameters
    ----------
    func : function from C to C
        The function which generates the fractal. 
    diff : function in one variable
        The derivative of func. 
    grid: array-like of shape (2,dim,dim)
        Grid with all start points for the algorithm.
    max-iterations: int
        Number of iterations before the algorithm terminates. 
        If it is exceeded, the function expects divergence.
    border: float
        Required distance for the calculated root to the 
        actual root in order to terminate.

    Returns
    -------
    roots : np.ndarray of float with shape (n+1,)
        Array of the roots of func. 
        Inculding [np.Inf,np.Inf] as last entry for divergence.
    indexes : np.ndarray of int with shape (dim,dim)
        At each entry the index in roots of the root which will be 
        approximated if the altorithem starts at the respective start 
        point in grid.
    iterations : np.ndarray of int with shape (dim,dim)
        At each entry the number of iterations until the recursion terminates.
    """
    start_time = time.perf_counter()
    
    # Init iteration variables
    calculate_step = np.vectorize(lambda point: catch(
                        lambda x:func(point)/x, diff(point), handle=np.Inf))
    value = grid[0]+1J*grid[1]
    dim = value.shape[1]
    iterations = np.zeros((dim,dim))
    done = np.zeros((dim,dim)).astype(bool)
    
    # Iteration step for those, where done is False.
    for i in range(max_iterations):
        value_old = value.copy()
        done_old = done.copy()
        value = value_old-np.array([[0 if done_old[i,j] 
                                     else calculate_step(value_old[i,j])
                                     for j in range(dim)] for i in range(dim)])
        done = np.logical_or(value==np.Inf, np.abs(value-value_old)<border)
        iterations[np.logical_and(done,np.logical_not(done_old))] = i+1
        if done.all(): break
    value[np.logical_not(done)] = np.Inf
    
    mid_time = time.perf_counter()
    print("Calculated results after", mid_time-start_time, "seconds.")
    
    # Calculate the set of roots
    data = value[value!=np.Inf]
    roots_set = []
    while len(data)>0:
        mask = np.isclose(data, data[0], atol=10*border)
        roots_set.append(data[mask])
        data = data[np.logical_not(mask)]
    roots = np.sort_complex([np.average(r_set) for r_set in roots_set])
    
    # make last calculations
    indexes = np.array([[len(roots) if value[i,j]==np.Inf
                         else np.argmin(np.abs(value[i,j]-roots))
                         for j in range(dim)] for i in range(dim)])
    roots = np.append(roots, np.Inf)
    
    end_time = time.perf_counter()
    print("Runntime:",end_time-start_time)
    return roots, indexes, iterations
    
