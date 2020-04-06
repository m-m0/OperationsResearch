import numpy as np
from scipy.optimize import minimize

# zielfunktion
def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1*x4*(x1+x2+x3)+x3

# inequality
def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0
# equality
def constraint2(x):
    sum_sq = 40
    for i in range(len(x)):
        sum_sq = sum_sq - x[i]**2
    return sum_sq

# initial guesses
x0 = [1,5,5,1]
print(objective(x0))

# define bounds and constraints
b = (1.0, 5.0)
bnds = (b,b,b,b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'eq', 'fun': constraint2}
cons = [con1,con2]

# solution
sol = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)
#print(sol)
#print(sol.fun)
print(sol.x)
