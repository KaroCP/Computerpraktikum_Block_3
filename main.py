'''
    The MAIN function of the Project. Here the user starts the plot.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

from function import Fractal
from data_collection import choose_fractal,chose_fractal_x_times_n


# In[2]

print("Welcome to our project")
# Funfact: the "f = " part ist necessary for the interaction.
f = Fractal(*chose_fractal_x_times_n())
# f = Fractal(*choose_fractal())    

print("""
Ready. 
You can interact with the plot.
==================================================
Press 'o' to zoome (a fix property) out.
Press 'r' to reset the zoom.
You have two zoom options:
    First you can zoom by drawing a rectangle.
    Second you can zoom with the mouse wheel 
        and move the plot with drag and drop.
        Use this option only when the canlulation is fast!
    You can switch the zoom options with 'z'.""")


# In[3] 


# In[10]



# In[100]
