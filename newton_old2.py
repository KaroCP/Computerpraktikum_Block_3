import numpy as np

# An Karo: Um das mit deinem Programm aufzurufen, müsstest du erst newton_approx_with_grid benutzen und das Ergebnis davon
# dann einmal durch sort_roots laufen lassen. Sort_roots gibt dir dann eine nxn-Matrix mit(2,.) Einträgen zurück. Erster Eintrag
# ist der Index der Nullstelle vom Startpunkt [y,x] im Anfangsgrid, zweiter Eintrag ist die Anzahl an Iterationen.
# Falls es mega lange braucht, versuch Zeile 119 auszukommentieren

''' TODO: für effizienteres Verfahren LGS J(x)*delta_x = -f(x) für delta_x lösen -> x = x+delta_x'''
def newton_approx_old2(f, f_diff, start_point, max_iterations = 100, border = 10**(-5)):
    """
    Newton Approximation of roots for complex functions
    Parameters
    ----------
    f : function
        function from R^2 to R^2 from which the root will be calculated.
    f_diff : Jacobi-matrix of f
    start_point: numpy-Array
        point from which the newton-approximation will start. Has dimension (2,.)
    max-iterations: int
        number of maximum iterations before the algorithm terminates. If it is exceeded, the function expects divergence
    border: float
        required distance of points from iterations i to i+1 for the algorithm to terminate
    Returns
    -------
    point : numpy-Array
        the calculated root
    iterations : int
        number of iterations until the algorithm terminated.
    """
    point = start_point
    for i in range(max_iterations):
        jacobi = f_diff(point[0],point[1])
        jacobi = np.linalg.inv(jacobi)
        temp_point = point
        point = point - np.matmul(jacobi, f(point[0],point[1]))
        if np.linalg.norm(point - temp_point) < border:
                return point, i+1
    return np.array([np.inf,np.inf]), max_iterations

def newton_approx_with_grid(f, f_diff, grid, max_iterations = 100, border = 10**(-5)):
    """
    Newton Approximation of roots for complex functions with meshgrid as input

    Parameters
    ----------
    f : function
        function from R^2 to R^2 from which the root will be calculated.
    f_diff : Jacobi-matrix of f
    grid: numpy-Array
        grid with all start_points for the algorithm. Has dimension (2,.) with each entry having dimension (n,n)
    max-iterations: int
        number of maximum iterations before the algorithm terminates. If it is exceeded, the function expects divergence
    border: float
        required distance of points from iterations i to i+1 for the algorithm to terminate

    Returns
    -------
    roots_grid : numpy-Array
        numpy-Array with each entry being a (3,.) numpy-Array, first entry is the x-coordinate of the root,
        second entry the y-coordinate of the root and the third entry the number of iterations to get the root. Has dimension (n,n)
    """
    x_grid = grid[0]
    y_grid = grid[1]
    roots_grid = np.zeros([x_grid.shape[0],x_grid.shape[1],3])
    for y in range(len(y_grid)):
        for x in range(len(x_grid)):
            start_point = np.array([x_grid[y,x],y_grid[y,x]])
            root_temp, iterations_temp = newton_approx_old2(f, f_diff, start_point, max_iterations = max_iterations, border = border)
            roots_grid[y,x] = np.array([root_temp[0],root_temp[1], iterations_temp])
    return roots_grid

def sort_roots(roots_grid, n, max_iterations = 100, border = 10**(-3)):
    """
    

    Parameters
    ----------
    roots_grid : numpy-Array
        matrix containing the calculated roots with newton approximation of different start-points. Has dimension (n,n), each entry has dimension (2,.)
    n : int
        degree of the function from which the newton algorithm calculated the roots
    max_iterations : int, optional
        number of max_iterations of the algorithm which calculated the roots_grid. The default is 100.
    border : float, optional
        maximum distance of two roots to be considered the same root. The default is 10**(-3).

    Returns
    -------
    roots_grid : numpy-Array
        numpy-Array with each entry being a (3,.) numpy-Array, first and second entry is the index of the root in roots
        and third entry the number of iterations. Has dimension (n,n)
    roots : list
        list with all roots of the function from wich the roots were calculated
    """
    roots = [[]]
    for i in range(n):
        roots.append([])
    initialized = False
    x, y = 0, 0
    while not initialized:
        temp_point = np.array([roots_grid[y,x][0],roots_grid[y,x][1]])
        temp_iteration = roots_grid[y,x][2]
        if temp_iteration < max_iterations:
            roots[0].append(temp_point)
            initialized = True
        else:
            if x == len(roots_grid)-1:
                x = 0
                y += 1
                if y == len(roots_grid):
                    roots[-1].append[np.inf]
                    return roots
            else:
                x += 1
    for y in range(len(roots_grid)):
        for x in range(len(roots_grid)):
            temp_point = np.array([roots_grid[y,x][0],roots_grid[y,x][1]])
            if roots_grid[y,x][0] == np.inf:
                roots_grid[y,x][0] == len(roots)-1
                roots_grid[y,x][1] == len(roots)-1
                continue
            for i in range(len(roots)-1):
                if roots[i] == []:
                    roots[i].append(temp_point)
                    roots_grid[y,x] = [i,i,roots_grid[y,x][2]]
                    break
                temp_root = np.array([sum(roots[i])[0]/len(roots[i]),sum(roots[i])[1]/len(roots[i])])
                distance = np.linalg.norm(temp_point-temp_root)
                if distance < border:
                    roots[i].append(temp_point)
                    roots_grid[y,x] = [i,i,roots_grid[y,x][2]]
                    break
    for i in range(len(roots)-1):
        roots[i] = sum(roots[i])/len(roots[i])
    roots[-1] = np.array([np.inf, np.inf])
    return roots_grid, roots