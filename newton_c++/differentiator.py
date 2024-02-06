# Lambdafunktionen, zb:
f1 = lambda x:x**3-1
#können hier abgeleitet werden und werden als solche wieder ausgegeben (nur eindimensionale eingaben der "f" funktion möglich)

from sympy.parsing.sympy_parser import parse_expr
import sympy
from sympy import sympify

# function ist eine lambda function
def ableitung (function):
    return sympy.lambdify(sympy.symbols("z"),sympy.diff(parse_expr(str(function(sympy.symbols("z"))), transformations=['all']), "z"))

   
# testresultat :
#print(ableitung(f1)(1)) # sollte 3*z^2 sein

#falls keine lambdafunkion rauskommen soll, sondern sympy.obj, kann einfach die "sympy.lambdify(..) rausgenommen werden"



# hier kommt karos anfrage für eine konsolen eingabe eines strings (zb x^3 ...)

def choose_any_fractal_function():
    print("""
please input your function that mapps x to some complex value, ie for example x^3-1""")
    temporary_bool = True
    while temporary_bool: 
        input1 = input("->")
        try:
            f = sympify(input1)
            print(f)
            diff = sympy.diff(f, sympy.Symbol("x"))
            label = input1
            temporary_bool = False
            print("function parsed!")
            return sympy.lambdify(sympy.Symbol("x"), f),sympy.lambdify(sympy.Symbol("x"), diff),label
        except:
            print("please enter parsable expression")

print(choose_any_fractal_function())
    