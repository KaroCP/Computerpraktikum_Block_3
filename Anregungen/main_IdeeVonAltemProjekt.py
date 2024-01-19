'''
Main programm
Run the program and interact with the consol.
'''

import inout
import userinterface


print("Welcome to our interpolation project")
print("""
========================================
Images:
    A1
    data1
    data2
    data3
    data4
    dragoncurve7
    dragoncurve10
*   f(x)
*   hilbert4
    inf
*   mandelbrot10
    mandelbrot100
    pi
    Q 
Videos:
*   clock
    reversedclock
Console:
*   console
""")

print("Input which Image should be shown")
print("e.g. 'f(x)' or 'console'")
print("Check the * out, they're impressive")

dataset = input(" > ")
if dataset == "clock":
    points = inout.clock()
elif dataset == "reversedclock":
    points = inout.reversedclock()
elif dataset == "console":
    points = inout.import_data_from_console(True)
else:
    points = inout.import_data_from_csv(".\\csv\\"+ dataset +".csv")

print("""
========================================
Methods:
1) linear
2) trigonometric
3) Cubic spline (equidistant)
4) Cubic spline (euclidian distant improved)
5) Points (supressed if there too much points)
6) - and Text for Points (supressed if there too much points)
7) - and Coordinate for Points
8) - and Interaction for Points 
""")

print("Input which methods should be shown")
print("e.g '1236' or '156'")
methods = input(" > ")
print()

plotmethods = [(str(i) in methods) for i in range(1,9)]

ui = userinterface.Userinterface(
    points,
    plotargs=plotmethods,
    )

print("""
========================================
Inputs (Mouse/Keyboard):
    id of method is pressed: Toggle interpolation method
    'z' is pressed: Print coordinates of the points. Only possible if 
        there are not to many points.
if interactive is active: (does not work on touchpad, only on real mouse)
    press 'a' and click: to add a point
    press 'd' and click: to delete a points
    drag a point: to drag a points
""")

if dataset == "clock" or dataset == "reversedclock":
    # Renew the plot to update the time.
    while ui.isVisible():
        if dataset == "clock":
            ui.set_data_points(inout.clock())
        else:
            ui.set_data_points(inout.reversedclock())
