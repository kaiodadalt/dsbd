import numpy as np
from scipy.special import roots_hermite

def integrand(x, lam):
    return lam * np.exp(- (x - lam)**2)

def gauss_hermite_integration(func, lam, n_points):
    # Calcula os nós e os pesos para a quadratura Gauss-Hermite
    nodes, weights = roots_hermite(n_points)

    # Ajusta os limites de integração de -infinito a +infinito para a faixa dos nós gerados
    integral = 0.0
    for i in range(n_points):
        integral += weights[i] * func(nodes[i], lam)

    return integral

# Parâmetros da integral
lam = 0.091
n_points = 21

# Calcula a integral
result = gauss_hermite_integration(integrand, lam, n_points)

print(round(result, 3))
