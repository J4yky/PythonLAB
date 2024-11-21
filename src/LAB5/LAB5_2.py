from scipy.optimize import fsolve
import numpy as np

def equations(vars):
    x, y = vars
    first_Equation = x**2 + 2 * x * y**2 -40
    second_Equation = 2 * x**2 - 3 * y**2 + 19
    return [first_Equation, second_Equation]

value_guess = np.array([1, 1])

result = fsolve(equations, value_guess)

x, y = result

print(f"x = {x:.5f}, y = {y:.5f}")