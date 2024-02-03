'''
The MAIN function of the Project. Here the user starts the plot.
'''
#!/usr/bin/env python
# coding: utf-8

# In[1]

from fractal import Fractal
from data_collection import chose_fractal_x_times_n,choose_fractal_from_data


# In[2]

print("Welcome to our project")
fix_data = True
if fix_data: f = Fractal(*choose_fractal_from_data())
else: f = Fractal(*chose_fractal_x_times_n())
# Funfact: the "f = " part ist necessary for the interaction.


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


# In[3] 


# In[10]



# In[100]
