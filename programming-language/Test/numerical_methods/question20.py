import numpy as np

# Função f e sua derivada em relação a μ
def f(mu, y):
    n = len(y)
    result = 0
    for yi in y:
        term1 = yi * np.log(yi / 10 / mu)
        term2 = (10 - yi) * np.log((10 - yi) / 10 / (1 - mu))
        result += 2 * (term1 + term2)
    return result - 3.84

def df(mu, y):
    n = len(y)
    result = 0
    for yi in y:
        term1 = yi / mu - (10 - yi) / (1 - mu)
        term2 = yi / (mu ** 2) + (10 - yi) / ((1 - mu) ** 2)
        result += 2 * term1 * term2
    return result

# Método de Newton para encontrar a raiz
def newton_method(y, mu_guess, epsilon=0.0001, max_iterations=1000):
    mu = mu_guess
    for _ in range(max_iterations):
        delta_mu = f(mu, y) / df(mu, y)
        mu -= delta_mu
        if abs(delta_mu) < epsilon:
            return mu
    return mu

# Valores de y fornecidos
y = [4, 6, 5, 7, 7, 2, 5, 7, 5, 5]

# Chute inicial
mu_guess = 0.5

# Encontrar a raiz
raiz = newton_method(y, mu_guess)

print("A raiz a direita do ponto crítico é:", round(raiz, 3))