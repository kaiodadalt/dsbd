def f(x):
    return x ** 3 - 155


def bisection_method(f, a, b, tol=1e-4, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    x_prev = a
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(c - x_prev) < tol:
            return c
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        x_prev = c

    raise RuntimeError("Maximum number of iterations reached")


# Intervalo inicial
a, b = 5, 6

# Encontrar a raiz
root = bisection_method(f, a, b)
print(f"A raiz cúbica de 155 é aproximadamente: {root:.3f}")
