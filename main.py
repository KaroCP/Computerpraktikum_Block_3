'''
    The MAIN function of the Project. Here the user starts the plot.'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

from function import Fractal
from data_collection import choose_fractal


# In[2]

print("Welcome to our project")
# Funfact: the "f = " part ist necessary for the interaction.
f = Fractal(*choose_fractal())    
print("""
========================================
You can interact with the plot.
Press at some point the left mouse button, draw the rectangle and 
    release the mousebutton at the desired location to zoom in. 
    The drawn recktangle will be the new shown part.
Press 'o' to zoome (a fix property) out.
Press 'r' to reset the zoom.
Press 'z' to switch to [zoom with the mouse wheel and moving the plot 
                        with drag and drop - use only if the 
                        calculation is fast!] and back""")



# In[3] 


# In[10]



# In[100]
