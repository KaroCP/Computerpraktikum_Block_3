# Lambdafunktionen, zb:
f1 = lambda x:x**3-1
#können hier abgeleitet werden und werden als solche wieder ausgegeben (nur eindimensionale eingaben der "f" funktion möglich)

from sympy.parsing.sympy_parser import parse_expr
import sympy

# function ist eine lambda function
def ableitung (function):
    return sympy.lambdify(sympy.symbols("z"),sympy.diff(parse_expr(str(function(sympy.symbols("z"))), transformations='all'), "z"))

   
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
            f = lambda x:eval(input1.replace("^", "**"))
            diff = ableitung(f)
            label = input1
            return f,diff,label
            temporary_bool = False
        except:
            print("please enter parsable expression")

print(choose_any_fractal_function())
    