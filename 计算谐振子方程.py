import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
omega = sp.symbols('w')
f = sp.Function('f')

equation = f(x).diff(x,2) + f(x)*omega**2
solution = sp.dsolve(equation,f(x))

print(solution)
sp.pprint(solution)