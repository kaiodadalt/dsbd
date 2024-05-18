import numpy as np
from scipy.special import roots_legendre

# Função a ser integrada
def integrand(y, alpha, beta):
    return beta**alpha * y**(alpha - 1) * np.exp(-beta * y)

# Parâmetros dados
a = 0.1
b = 8.1
alpha = 2
beta = 3

# Número de pontos de Gauss-Legendre
n_points = 15

# Obtenção dos pontos e pesos de Gauss-Legendre
points, weights = roots_legendre(n_points)

# Transformação da integral de [a, b] para [-1, 1]
def gauss_legendre_integral(func, a, b, points, weights, alpha, beta):
    t = 0.5 * (points + 1) * (b - a) + a
    integral = 0.5 * (b - a) * np.sum(weights * func(t, alpha, beta))
    return integral

# Cálculo da integral
result = gauss_legendre_integral(integrand, a, b, points, weights, alpha, beta)
result = round(result, 3)

print(result)
