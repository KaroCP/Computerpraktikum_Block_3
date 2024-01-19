import numpy as np

''' TODO: für effizienteres Verfahren LGS J(x)*delta_x = -f(x) für delta_x lösen -> x = x+delta_x'''
def newton_approx(f, f_diff, start_point, zeroset, max_iterations = 200, border = 10**(-7)):
    """
    Newton Approximation of roots for complex numbers

    Parameters
    ----------
    f : function
        Function from C to C from which the root will be calculated.
    f_diff : Jacobi-matrix of f
    start_point: numpy-Array
        point from which the newton-approximation will start. Has dimension (2,.)
    zeroset: numpy-Array
        array with all the actual roots of the function f
    max-iterations: int
        number of iterations before the algorithm terminates. If it is exceeded, the function expects divergence
    border: float
        required distance for the calculated root to the actual root in order to terminate
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
        jacobi = np.array([[f_diff[0][0](x[0],x[1]), f_diff[0][1](x[0],x[1])],[f_diff[1][0](x[0],x[1]), f_diff[1][1](x[0],x[1])]])
        jacobi = np.linalg.inv(jacobi)
        x = x - np.matmul(jacobi, f(x[0],x[1]))
        for i in zeroset:
            if np.linalg.norm(x, i) < border:
                return i, iterations
        iterations += 1
    return np.inf, iterations


def calculate_ns(newton, points): # Karos komisches zeugs
    value = np.array(f_newton(points[:,:,0],points[:,:,1])).transpose(1,2,0)
    return None

# newton_approx mit allen werten aufrufen

    
# Nullstellenmenge berechnen
    
# Array in farben übersetzen