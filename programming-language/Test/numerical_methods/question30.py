import numpy as np

# Parâmetros
lambda_value = 7988
alpha = np.log(3) / 0.12 + 1

# Função a ser integrada
def integrand(x):
    return np.exp(-alpha * x)

# Pontos e pesos da quadratura de Gauss-Laguerre
n = 20
nodes, weights = np.polynomial.laguerre.laggauss(n)

# Cálculo da integral usando a quadratura de Gauss-Laguerre
integral_value = sum(weights * integrand(nodes))

# Multiplicando pelo fator constante fora da integral
result = (lambda_value / 0.12) * integral_value
print(f"O valor da integral é aproximadamente: {result:.3f}")
