import numpy as np

''' TODO: für effizienteres Verfahren LGS J(x)*delta_x = -f(x) für delta_x lösen -> x = x+delta_x'''
def newton_approx(f, f_diff, start_points, max_iterations = 200, border = 10**(-3)):
    """
    Newton Approximation of roots for complex numbers

    Parameters
    ----------
    f : function
        Function from R^2 to R^2 from which the root will be calculated.
    f_diff : numpy-Array
        Jacobi-Matrix of f
    start_points: numpy-Array
        Array with all start_points. Has dimension (2,.) with each entry being an nxn-Array. The first one having all x and the second one having all y coordinates.
    zeroset: numpy-Array
        array with all the actual roots of the function f
    max-iterations: int
        number of iterations before the algorithm terminates. If it is exceeded, the function expects divergence
    border: float
        required distance for the calculated root to the actual root in order to terminate
    Returns
    -------
    i : int
        The index of the root, which is approximated, in zeroset.
    iterations : int
        Number of iterations until the recursion terminates.

    """
    y_dim,x_dim = start_points[0].shape[0], start_points[0].shape[1]
    root_help = []
    roots = []
    point_help = np.zeros([y_dim,x_dim,2])
    iterations_help = np.zeros([y_dim,x_dim])
    for y in range(y_dim):
        for x in range(x_dim):
            point = np.array([start_points[0][y,x], start_points[1][y,x]])
            iterations = 0
            stop_iterations = False
            while iterations < max_iterations and stop_iterations == False:
                jacobi = f_diff(point[0],point[1])
                jacobi = np.linalg.inv(jacobi)
                point_temp = point
                point = point - np.matmul(jacobi, f(point[0],point[1]))
                if np.linalg.norm(point, point_temp) < border:
                    iterations_help[y,x] = 0
                    stop_iterations == True
            for i in root_help:
                if np.linalg.norm(point, sum(i)/len(i)) < border:
                    i.append(point)
                else:
                    root_help.append([point])
            iterations += 1
            point_help[y,x] = point
        
    for i in root_help:
        if len(i) > 9:
            roots.append(sum(i)/len(i))
    roots.append(np.inf)
    for y in range(y_dim):
        for x in range(x_dim):
            for i in range(len(roots)):
                if np.linalg.norm(point_help[x,y], roots[i]) < border:
                    point_help[x,y] = i
                    break
                else:
                    point_help[x,y] = len(roots)
    return point_help, roots



# def calculate_ns(newton, points): # Karos komisches zeugs
#     value = np.array(f_newton(points[:,:,0],points[:,:,1])).transpose(1,2,0)
#     return None

# newton_approx mit allen werten aufrufen

    
# Nullstellenmenge berechnen
    
# Array in farben übersetzen