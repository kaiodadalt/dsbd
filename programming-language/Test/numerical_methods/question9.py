import numpy as np


# Função objetivo e sua derivada
def f(mu, y):
    n = len(y)
    result = 0
    for i in range(n):
        result += ((y[i] - mu) / mu) ** 2 / y[i]
    return result - 0.5


def df(mu, y):
    n = len(y)
    result = 0
    for i in range(n):
        result += -2 * (y[i] - mu) / (mu ** 2 * y[i])
    return result


# Método de Newton
def newton_method(y, initial_guess, epsilon=0.0001):
    mu = initial_guess
    delta = np.inf

    while abs(delta) >= epsilon:
        mu_new = mu - f(mu, y) / df(mu, y)
        delta = mu_new - mu
        mu = mu_new

    return mu


# Dados
y = np.array([10.179, 10.073, 10.505, 10.022, 10.041, 10.557, 10.147, 10.408, 9.785, 9.860])

# Escolha de valor inicial
initial_guess = 10.0

# Resolvendo
root = newton_method(y, initial_guess)

# Exibição do resultado com três casas decimais
print("Valor da raiz:", round(root, 3))
