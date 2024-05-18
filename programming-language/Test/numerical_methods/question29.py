import numpy as np

def f(x):
    return x**3 - 2.2*x**2 - 2.15*x + 5.1

def regula_falsi(f, a, b, tol=1e-4, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    x_prev = a
    for i in range(max_iter):
        x = b - (f(b) * (b - a)) / (f(b) - f(a))

        if abs(x - x_prev) < tol:
            return x

        if f(x) * f(a) < 0:
            b = x
        else:
            a = x

        x_prev = x

    raise RuntimeError("Maximum number of iterations reached")

# From the previous analysis, we use the interval [a, b] = [-2, -1]
a, b = -2, -1

# Applying the regula falsi method
root = regula_falsi(f, a, b)
print(f"The root is approximately: {root:.3f}")
