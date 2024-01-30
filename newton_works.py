'''
Newton approximation form Karo.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
import warnings
warnings.filterwarnings("ignore")

from data_collection import catch

# In[2]

def newton_with_matrices(func, diff, grid, max_iterations, border):
    """
    Newton approximation of roots for complex functions.
    Calculating the resluts simultanuously by using matrixmultiplication.

    Parameters
    ----------
    func : function
        Function from R^2 to R^2 from which the root will be calculated.
    diff : function
        At each point the Jacobi-matrix of f.
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
    roots : np.ndarray of float with shape (n+1,2)
        Array of the roots of func. 
        Inculding [np.Inf,np.Inf] as last entry for divergence.
    indexes : np.ndarray of int with shape (dim,dim)
        At each entry the index in roots of the root which will be 
        approximated if the altorithem starts at the respective start 
        point in grid.
    iterations : np.ndarray of int with shape (dim,dim)
        At each entry the number of iterations until the recursion terminates.
    """
    
    def calculate_step(point):
        return catch(lambda x:np.matmul(np.linalg.inv(x),func(*point)),
                     diff(*point), handle=np.array([np.Inf,np.Inf]))
    value = np.array(grid).copy().transpose(1,2,0)
    dim = value.shape[1]
    iterations = np.zeros((dim,dim))
    mask = np.zeros((dim,dim))
    
    for i in range(max_iterations):
        value_old = value.copy()
        mask_old = mask.copy()
        value = value_old-np.array([[[0,0] if mask_old[i,j] 
                                      else calculate_step(value[i,j])
                                      for j in range(dim)] for i in range(dim)])
        mask = np.logical_or(value[:,:,0]==np.Inf,
                             np.linalg.norm(value-value_old,axis=2)<border)
        iterations[(mask.astype(int)-mask_old.astype(int)).astype(bool)] = i+1
        if mask.all(): break
    value[(1-mask.astype(int)).astype(bool)] = [np.Inf,np.Inf]
    
    roots = get_roots_from_data(value.reshape((dim*dim,2)), 10*border)
    indexes = np.array([[len(roots) if value[i,j,0]==np.Inf
                         else np.argmin(np.linalg.norm(value[i,j]-roots,axis=1))
                         for j in range(dim)] for i in range(dim)])
    roots = np.append(roots, [[np.Inf,np.Inf]],axis=0)
    return roots, indexes, iterations
    

def get_roots_from_data(data, border):
    """
    Helpfunction for calculating the set of roots from a given data set.

    Parameters
    ----------
    data : array-like of float with shape (N,2)
        Dataset of near approximations of roots.
    border : float
        Tolerance how far the points are summarized.
        Not the border of newton_with_matrizes.

    Returns
    -------
    roots : np.ndarray of float with shape (n,2)
        Array of the roots of func.
    """
    roots_set = []
    for point in data:
        if np.Inf not in point and roots_set!=[]:
            appended = False
            for r_set in roots_set:
                if np.min(np.linalg.norm(np.array(r_set)-point,axis=1))<border:
                    r_set.append(point)
                    appended = True
                    break
            if not appended:
                roots_set.append([point])
        elif point[0]!=np.Inf:
            roots_set = [[data[0]]]
    # i = 0
    # while i<len(roots_set):
    # TODO summarize those who ars equal, dont pop new data!
    if len(roots_set[0])==1: 
        roots_set.pop(0)
    roots = np.array([np.average(r_set,axis=0) for r_set in roots_set])
    roots = roots[np.lexsort(-roots.T)]
    return roots
    
