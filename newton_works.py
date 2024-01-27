'''
Newton approximation. The compatible but not-current Modul.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
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
        # jacobi = np.array([[f_diff(x[0],x[1])[0][0], f_diff(x[0],x[1])[0][1]],[f_diff(x[0],x[1])[1][0], f_diff(x[0],x[1])[1][1]]])
        jacobi = f_diff(x[0],x[1])
        jacobi = np.linalg.inv(jacobi)
        x = x - np.matmul(jacobi, f(x[0],x[1]))
        for k,ns in enumerate(zeroset):
            if np.linalg.norm(x-ns) < border:
                return k, iterations
        iterations += 1
    return len(zeroset), iterations


# In[3]
    
def newton(func, f_diff, grid, max_iterations, border):
    # grid directly from np.meshgrid
    grid = np.array(grid).copy().transpose(1,2,0) #now itw a matrix containing (2,) arrays
    n = grid.shape[1]
    Jacobi = np.array([[catch(np.linalg.inv,f_diff(*grid[i,j])) for j in range(n)] for i in range(n)])
    iterations = np.zeros((n,n))
    mask = Jacobi[:,:,0,0] == np.infty
    
    for i in range(max_iterations):
        grid_old = grid.copy()
        mask_old = mask.copy()
        f_grid = np.array(func(grid_old[:,:,0],grid_old[:,:,1])).transpose(1,2,0)
        grid = np.array([[grid_old[i,j] if mask_old[i,j] else Jacobi[i,j]@f_grid[i,j] for j in range(n)] for i in range(n)])
        # grid = np.array([[grid_old[i,j] if mask_old[i,j] else Jacobi[i,j]@func(*grid_old[i,j]) for j in range(n)] for i in range(n)])
        mask = np.linalg.norm(grid-grid_old,axis=2)<border
        grid = np.nan_to_num(grid,nan=np.infty,posinf=np.infty)
        mask[grid[:,:,0]==np.infty] = True
        mask[grid[:,:,1]==np.infty] = True
        # print((mask.astype(int)-mask_old.astype(int)).astype(bool),i)
        iterations[(mask.astype(int)-mask_old.astype(int)).astype(bool)] = i+1
        # print(mask,i)
        if mask.all(): break
    grid[mask] = np.infty
    return grid, iterations
        
# In[10]

# dim=15
# # grid = np.array([[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]]])+[1,1]#.transpose(2,0,1)
# grid = np.array(np.meshgrid(np.linspace(-2,2,dim),np.linspace(-2,2,dim)))#.transpose(1,2,0)
# f = lambda z:np.power(z,3)-1
# f_ = lambda z:3*z**2
# func = lambda a,b:[np.real(f(a+b*1J)), np.imag(f(a+b*1J))]
# f_diff = lambda a,b:[[np.real(f_(a+b*1J)), np.real(f_(a+b*1J)*1J)],
#                      [np.imag(f_(a+b*1J)), np.imag(f_(a+b*1J)*1J)]]
# # Jacobi = np.array([[np.linalg.inv(f_diff(*grid[i,j])) for j in range(dim)] for i in range(dim)])
# # mask = np.array([[0,1,0],[1,1,1],[0,1,1]])


# roots, iterations = newton(func,f_diff,grid,30,10e-7)
# print(iterations)

# In[11]

# roots_here = roots.copy()
# print(roots_here)
# roots_here = np.nan_to_num(roots_here,nan=np.infty)
# print(roots_here)
# print(roots_here[5,6,0])
# roots_here = np.sort(roots_here.reshape((dim*dim,2)) ,axis=1)

# In[12]

# i=7
# grid = np.array(np.meshgrid(np.linspace(1,2,dim),np.linspace(0,1,dim))).transpose(1,2,0)
# grid_old = grid.copy()
# mask_old = np.zeros((dim,dim))#
# # mask_old[:,1] = np.ones((n,))
# f_grid = np.array(func(grid[:,:,0],grid[:,:,1])).transpose(1,0,2) #not (1,2,0) because dot sums over the secondlast entry
# grid = np.array([[grid[i,j] if mask_old[i,j] else Jacobi[i,j]@f_grid[i,:,j] for j in range(dim)] for i in range(dim)])
# # grid = np.where(mask,grid,np.diagonal(np.diagonal(np.dot(Jacobi,f_grid),axis1=0,axis2=3),axis1=0,axis2=2).transpose(1,2,0))
# mask1 = np.linalg.norm(grid-grid_old,axis=2)<10e-1
# grid2 = np.array([[grid[i,j] if mask1[i,j] else Jacobi[i,j]@f_grid[i,:,j] for j in range(dim)] for i in range(dim)])
# mask2 = np.linalg.norm(grid2-grid,axis=2)<10e-1
# # value = newton(func,f_diff,grid,32,30)
# # print(grid[(mask,0)])
# # print(func(grid[mask,0],grid[mask,1]))
# iterations = np.zeros(grid.shape[1:])
# # print(mask2.astype(int)-mask1.astype(int))
# iterations[mask2.astype(int)-mask1.astype(int)] = i        
# print(iterations)