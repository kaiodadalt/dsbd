import numpy as np


# Funções que representam as equações do sistema
def f(x, y):
    return x ** 3 + y - 1


def g(x, y):
    return y ** 3 - x + 1


# Derivadas parciais das funções em relação a x e y
def df_dx(x, y):
    return 3 * x ** 2


def df_dy(x, y):
    return 1


def dg_dx(x, y):
    return -1


def dg_dy(x, y):
    return 3 * y ** 2


# Implementação do método de Newton
def newton_method(x0, y0, epsilon=0.0001, max_iterations=100):
    x = x0
    y = y0
    iterations = 0

    while True:
        fx = f(x, y)
        gy = g(x, y)

        J = np.array([[df_dx(x, y), df_dy(x, y)],
                      [dg_dx(x, y), dg_dy(x, y)]])

        J_inv = np.linalg.inv(J)

        delta = np.dot(J_inv, np.array([-fx, -gy]))

        x += delta[0]
        y += delta[1]

        iterations += 1

        if np.linalg.norm(delta) < epsilon or iterations >= max_iterations:
            break

    return x, y


# Escolha dos valores iniciais
x0 = 1
y0 = 1

# Resolução do sistema de equações
x_hat, y_hat = newton_method(x0, y0)

print("Raízes encontradas:")
print("x̂ = {:.3f}".format(x_hat))
print("ŷ = {:.3f}".format(y_hat))
