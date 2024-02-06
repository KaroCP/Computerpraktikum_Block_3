import time
import numpy as np
import matplotlib.pyplot as plt
from data_collection import *
from fractal import *
from newton import *

max_tests = 50


f_func = f1_func
f_diff = f1_diff
lims = np.array([[-1, -1], [1, 1]])
density = 30
grid = np.meshgrid(np.linspace(lims[:,0], density),
                   np.linspace(lims[:,1], density))
max_iterations = 50
tolerance = 10e-7
density_linspace = np.linspace(5,100, num = 20)

# plot_time = []
# for j in range(len(density_linspace)):
#     print(j)
#     grid = np.meshgrid(np.linspace(lims[:,0], density_linspace[j]),
#                         np.linspace(lims[:,1], density_linspace[j]))
#     time_1 = []
#     for i in range(max_tests):
#         start_time = time.perf_counter()
#         newton_approximation(f_func, f_diff, grid, max_iterations, tolerance)
#         end_time = time.perf_counter() - start_time
#         time_1.append(end_time)
#     plot_time.append(sum(time_1)/len(time_1))

# timeplot, = plt.plot(density_linspace, plot_time)
# plt.xlabel = "density"
# plt.ylabel = "time"
# plt.legend()
# plt.show()

for i in range(max_tests):
    start_time = time.perf_counter()
    newton_approximation(f_func, f_diff, grid, max_iterations, tolerance)
    end_time = time.perf_counter() - start_time
    time_1.append(end_time)
print("newton_approximation of z^7-1 with\ndensity = {}\nmax_iterations = {}\ntolerance = {}\nneeded on average {} seconds"
      .format(density,max_iterations,tolerance,sum(time_1)/len(time_1)))

print("")

time_1 = []
density = 50
grid = np.meshgrid(np.linspace(lims[:,0], density),
                    np.linspace(lims[:,1], density))
for i in range(max_tests):
    start_time = time.perf_counter()
    newton_approximation(f_func, f_diff, grid, max_iterations, tolerance)
    end_time = time.perf_counter() - start_time
    time_1.append(end_time)
print("newton_approximation of z^7-1 with\ndensity = {}\nmax_iterations = {}\ntolerance = {}\nneeded on average {} seconds"
      .format(density,max_iterations,tolerance,sum(time_1)/len(time_1)))

print("")

time_1 = []
density = 80
grid = np.meshgrid(np.linspace(lims[:,0], density),
                    np.linspace(lims[:,1], density))
for i in range(max_tests):
    start_time = time.perf_counter()
    newton_approximation(f_func, f_diff, grid, max_iterations, tolerance)
    end_time = time.perf_counter() - start_time
    time_1.append(end_time)
print("newton_approximation of z^7-1 with\ndensity = {}\nmax_iterations = {}\ntolerance = {}\nneeded on average {} seconds"
      .format(density,max_iterations,tolerance,sum(time_1)/len(time_1)))

print("")

time_1 = []
density = 100
grid = np.meshgrid(np.linspace(lims[:,0], density),
                    np.linspace(lims[:,1], density))
for i in range(max_tests):
    start_time = time.perf_counter()
    newton_approximation(f_func, f_diff, grid, max_iterations, tolerance)
    end_time = time.perf_counter() - start_time
    time_1.append(end_time)
print("newton_approximation of z^7-1 with\ndensity = {}\nmax_iterations = {}\ntolerance = {}\nneeded on average {} seconds"
      .format(density,max_iterations,tolerance,sum(time_1)/len(time_1)))

# density = 100
# time2 = []
# for i in range(max_tests):
#     start_time = time.perf_counter()
#     frac = Fractal(f_func, diff = f_diff, label = "z^3-1", density = density, max_iteration = max_iterations, tolerance = tolerance)
#     frac.fast = False #TODO
#     frac.update(True)
#     end_time = time.perf_counter() - start_time
#     time2.append(end_time)
# print("Setting up the fractal with density = {} needed {} seconds".format(density, sum(time2)/len(time2)))