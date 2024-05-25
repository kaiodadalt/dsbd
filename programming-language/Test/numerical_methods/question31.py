import numpy as np
from scipy.special import roots_hermite

# Definindo o valor de lambda
lambda_value = 0.135

# Função a ser integrada
def integrand(x, lambda_value):
    return np.exp(-np.abs(x - lambda_value))

# Pontos e pesos da quadratura de Gauss-Hermite
n = 20
nodes, weights = roots_hermite(n)

# Ajustar os pontos para Gauss-Hermite
integral_value = sum(weights * integrand(nodes, lambda_value))

# Multiplicando pelo fator de ajuste da quadratura de Gauss-Hermite
result = lambda_value * integral_value * np.sqrt(np.pi)
print(f"O valor da integral é aproximadamente: {result:.3f}")
