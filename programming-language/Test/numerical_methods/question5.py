import numpy as np


# Função objetivo e sua derivada
def f(mu, y, m):
    n = len(y)
    result = 0
    for i in range(n):
        result += 2 * (y[i] * np.log(y[i] / (mu * m)) + (m - y[i]) * np.log((1 - y[i] / mu) / (1 - mu)))
    return result - 3.84


def df(mu, y, m):
    n = len(y)
    result = 0
    for i in range(n):
        result += 2 * ((y[i] - m) / (mu * (1 - mu * m)))
    return result


# Método do gradiente descendente
def gradient_descent(y, m, learning_rate=0.01, epsilon=0.0001):
    mu = 1.0  # Valor inicial
    delta = np.inf

    while abs(delta) >= epsilon:
        mu_new = mu - learning_rate * df(mu, y, m)
        delta = mu_new - mu
        mu = mu_new

    return mu


# Dados
y = np.array([4, 6, 5, 7, 7, 2, 5, 7, 5, 5])
m = np.mean(y)

# Resolvendo
root = gradient_descent(y, m)

# Exibição do resultado com três casas decimais
print("Valor da raiz:", round(root, 3))
