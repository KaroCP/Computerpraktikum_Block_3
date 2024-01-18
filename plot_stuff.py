#!/usr/bin/env python
# coding: utf-8

# In[1]

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()


# In[2]

density = 3
grid_template = np.array(np.meshgrid(np.linspace(0,1,density),
                            np.linspace(0,1,density))).transpose(1,2,0)
max_iteration = 8 #TODO (From) where should max_iterations be defined?


# In[3]

from colorsys import hsv_to_rgb
h = np.vectorize(hsv_to_rgb)

def get_color(f,value):
    hsv_data = value.copy().astype(float)
    hsv_data[:,:,0] = f.colors[hsv_data[:,:,0].astype(int)]
    mask = np.kron(np.any(hsv_data==1000, axis=2),np.ones(3)).reshape((density,density,3)).astype(bool)
    hsv_data[:,:,1] = np.array((hsv_data[:,:,1]/max_iteration/2+1/4))
    color = np.array(h(hsv_data[:,:,0],1,hsv_data[:,:,1])).T
    color[mask]=1
    return color


# In[5]

def plot(f,zoom=1,translation=0):
    """
    Plots the fractal structure on a grid.

    Parameters
    ----------
    f : Function
        Says from which function the structure is plotted.
    zoom : float, optional
        Variable to measure the zoom. The default is 1.
    translation : (2,) array of floats, optional
        Variable to measure the translation. The default is 0.
    """
    grid = zoom*grid_template+translation
    value = np.array(f.newton(grid[:,:,0],grid[:,:,1])).transpose(1,2,0)
    color = get_color(f,value)
    im = ax.imshow(color)
    return "TODO" # how to aktualize smoothly


# In[10]

from function import Function

# f = Function(np.sin,np.cos)
g = lambda x:x^3-1
g_diff = lambda x:3*x^2
g_0 = [1,-1/2+np.sqrt(3)*1J/2, -1/2-np.sqrt(3)*1J/2]
g = Function(g,g_diff,g_0)
# print(plot(g, zoom=2, translation=[1,0]))

# np.random.seed(1)
# a = np.random.randint(0,4,size=(density,density,2))
   

# In[100]



# In[101]

# import matplotlib.pyplot as plt
# import numpy as np

# t = np.linspace(0, 2 * np.pi, 1024)
# data2d = np.sin(t)[:, np.newaxis] * np.cos(t)[np.newaxis, :]
# data2d = np.array([[1,2,3],[2,0,4],[3,4,5]])

# plt.imshow(data2d)
# # fig, ax = plt.subplots()
# # im = ax.imshow(data2d)
# # ax.set_title('Pan on the colorbar to shift the color mapping\n'
# #              'Zoom on the colorbar to scale the color mapping')

# # fig.colorbar(im, ax=ax, label='Interactive colorbar')

# plt.show()


# In[102]

f = np.vectorize(lambda x,y,z: z if x<y else -z)
a = np.array([[[1,2,3],[2,1,3]],[[2,3,4],[2,3,-4]],[[0,4,3],[0,3,4]]])
b = np.array([0,0.25,0.5,0.75,1])
# print(a[:,:,0])
# print(a)
# print(f(a[:,:,0],a[:,:,1],a[:,:,2]))
# a = np.array([[[0.1,0.2,0.3],[0.2,0.1,0.3]],[[0.2,0.3,0.4],[0.2,0.3,-0.4]],[[0.5,0.4,0.3],[0.5,0.3,0.4]]])
h = np.vectorize(hsv_to_rgb)
# print(np.array(h(a[:,:,0],a[:,:,1],a[:,:,2])).T)

# print(b[a[:,:,0]])
a = 10*np.array([[[np.inf,0.2,0.0],[np.inf,0.1,0.0]],[[0.3,0.3,0.1],[0.2,0.3,0]],[[0.0,0.0,0.3],[0.0,0.1,0.4]]])
