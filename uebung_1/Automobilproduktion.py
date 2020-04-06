import numpy as np
from scipy.optimize import minimize

def objective(x):
    return -(x[0]*3000 + x[1]*2000)

# Vormontage constraint
def constraint1(x):
    return (5*x[0] + 3*x[1]) - 180
# Endmontage constraint
def constraint2(x):
    return (3*x[0] + 3*x[1]) - 135

# initial guesses
x0 = [0, 100]

# define bounds and constraints
b = (0.0, float('inf'))
bnds = (b,b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = [con1,con2]

# solution
sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)
print(sol)
#print(sol.fun)
#print(sol.x)
