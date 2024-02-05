'''
The MAIN function of the Project. Here the user starts the plot.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

from fractal import Fractal
from data_collection import get_fractal


# In[2]


print("Welcome to our project")
frac = Fractal(*get_fractal())
frac.set_fast(False)
frac.recalculate = True
frac.update()
# Funfact: the "frac = " part ist necessary for the interaction.

print("""Ready.
      
You can interact with the plot.
==================================================
Press 't' to toggle an infotextbox on and of.
You have two zoom options:
    First you can zoom by drawing a rectangle.
    Second you can zoom with the mouse wheel 
        and move the plot with drag and drop.
        Use this option only when the canlulation is fast!
    You can switch the zoom options with 'z'.
Press 'b' to zoome back to the last zoom settings.
Press 'o' to zoome (a fix property) out.
Press 'r' to reset the zoom.
""")

if frac.pointer!=None:
    while frac.isVisible():
        frac.kino()
    
