'''
Newton approximation. The compatible but not-current Modul.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
# import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

from data_collection import catch

# In[2]

''' TODO: für effizienteres Verfahren LGS J(x)*delta_x = -f(x) für delta_x lösen -> x = x+delta_x'''
def newton_approx(f, f_diff, start_point, zeroset, max_iterations = 200, border = 10**(-7)):
    """
    Newton Approximation of roots for complex functions.

    Parameters
    ----------
    f : function
        Function from C to C from which the root will be calculated.
    f_diff : function
        At each point the Jacobi-matrix of f.
    start_point: array-like
        Point from which the newton-approximation will start.
        Has dimension (2,)
    zeroset: array-like
        Array with all the actual roots of the function f.
    max-iterations: int
        number of iterations before the algorithm terminates. 
        If it is exceeded, the function expects divergence.
    border: float
        Required distance for the calculated root to the 
        actual root in order to terminate.
    Returns
    -------
    root : int
        The index of the root, which is approximated, in zeroset.
    iterations : int
        Number of iterations until the recursion terminates.
    """
    iterations = 0
    x = start_point
    while iterations < max_iterations:
        jacobi = f_diff(x[0],x[1])
        jacobi = np.linalg.inv(jacobi)
        x = x - np.matmul(jacobi, f(x[0],x[1]))
        for k,ns in enumerate(zeroset):
            if np.linalg.norm(x-ns) < border:
                return k, iterations
        iterations += 1
    return len(zeroset), iterations


# In[3]
    
def newton_with_matrices(func, f_diff, grid, max_iterations, border):
    value = np.array(grid).copy().transpose(1,2,0) #now itw a matrix containing (2,) arrays
    dim = value.shape[1]
    Jacobi = np.array([[catch(np.linalg.inv,f_diff(*value[i,j]),
                              handle=np.array([[np.Inf,np.Inf],[np.Inf,np.Inf]])) 
                        for j in range(dim)] for i in range(dim)])
    iterations = np.zeros((dim,dim))
    mask = Jacobi[:,:,0,0] == np.Inf
    value[mask] = [np.Inf,np.Inf]
    
    for i in range(max_iterations):
        value_old = value.copy()
        mask_old = mask.copy()
        Jacobi = np.array([[catch(np.linalg.inv,f_diff(*value[i,j]),
                                  handle=np.array([[np.Inf,np.Inf],[np.Inf,np.Inf]])) 
                            for j in range(dim)] for i in range(dim)])
        value = value_old-np.array([[[0,0] if mask_old[i,j] 
                          else np.matmul(Jacobi[i,j],func(*value_old[i,j])) 
                          for j in range(dim)] for i in range(dim)])
        mask = np.logical_or(Jacobi[:,:,0,0]==np.Inf,np.linalg.norm(value-value_old,axis=2)<border)
        iterations[(mask.astype(int)-mask_old.astype(int)).astype(bool)] = i+1
        if mask.all(): break
    value[(1-mask.astype(int)).astype(bool)] = [np.Inf,np.Inf]
    
    roots = get_roots_from_data_with_matrices(value, border)
    indexes = np.array([[len(roots) if value[i,j,0]==np.Inf
                         else np.argmin(np.linalg.norm(value[i,j]-roots,axis=1))
                         for j in range(dim)] for i in range(dim)])
    roots = np.append(roots, [[np.Inf,np.Inf]],axis=0)
    return indexes, iterations, roots
    

def get_roots_from_data_with_matrices(value, border):
    dim = value.shape[1]
    data = value.reshape((dim*dim,2))
    roots_set = []
    for point in data:
        if np.Inf not in point and roots_set!=[]:
            appended = False
            for r_set in roots_set:
                if np.min(np.linalg.norm(np.array(r_set)-point,axis=1))<10*border:
                    r_set.append(point)
                    appended = True
                    break
            if not appended:
                roots_set.append([point])
        elif point[0]!=np.Inf:
            roots_set = [[data[0]]]
    if len(roots_set[0])==1: 
        roots_set.pop(0)
    roots = np.array([np.average(r_set,axis=0) for r_set in roots_set])
    roots = roots[np.lexsort(roots.T)]
    return roots
    

# In[10]

# dim=100
# # grid = np.array([[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]])+[1,1]#.transpose(2,0,1)
# lims = 2
# grid = np.array(np.meshgrid(np.linspace(-lims,lims,dim),np.linspace(-lims,lims,dim)))#.transpose(1,2,0)
# f = lambda z:np.power(z,3)-1
# f_ = lambda z:3*z**2
# func = lambda a,b:[np.real(f(a+b*1J)), np.imag(f(a+b*1J))]
# f_diff = lambda a,b:[[np.real(f_(a+b*1J)), np.real(f_(a+b*1J)*1J)],
#                       [np.imag(f_(a+b*1J)), np.imag(f_(a+b*1J)*1J)]]
# # Jacobi = np.array([[np.linalg.inv(f_diff(*grid[i,j])) for j in range(dim)] for i in range(dim)])
# # mask = np.array([[0,1,0],[1,1,1],[0,1,1]])


# # roots_index, iterations, roots = newton(func,f_diff,grid,100,10e-7)
# back = newton_with_matrices(func,f_diff,grid,100,10e-7)
# print(len(back))

# In[11]

# a = np.array([[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]])
# A = np.array([[np.Inf,np.Inf],[np.Inf,np.Inf]])
# A = a.reshape(3*3,2)
# print(A)
# b = np.array([-1,2])
# c = np.linalg.norm(b-A,axis=1)
# # print(np.argmin(c))
# # print(c)
# mask = np.array([[0,1,1],[1,1,1],[0,1,0]]).astype(bool)
# a[mask]=[5,5]
