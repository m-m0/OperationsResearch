import numpy as np
from scipy.optimize import minimize

# zielfunktion
def objective(x):
    x1 = x[0]
    x2 = x[1]
    return -(10*x1 + 20*x2)

# Maschinenrestriktion
def constraint1(x):
    return (x[0] + x[1]) - 100
# Rohstoffrestriktion
def constraint2(x):
    return (6*x[0] + 9*x[1]) - 720

# initial guesses
x0 = [0, 80]
print(objective(x0))

# define bounds and constraints
b = (0.0, float('inf'))
bnds = (b,b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = [con1,con2]
#
# # solution
sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)
print(sol)
#print(sol.fun)
print(sol.x)
