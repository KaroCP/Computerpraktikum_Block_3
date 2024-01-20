'''
Newton approximation. The compatible but not-current Modul.
'''
# TODO Can we implement some algorithm to calculate the set of roots?

import numpy as np

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

    
