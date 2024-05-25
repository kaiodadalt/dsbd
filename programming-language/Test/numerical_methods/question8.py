from scipy import integrate
import numpy as np

# Definição da função a ser integrada
def integrand(y):
    k = 5
    lam = 10
    return (5 / 10) * ((y / 10)**(5 - 1)) * np.exp(-(y / 10)**5)

# Limites de integração
a = 0.1
b = 13.1

# Número de pontos de integração
n_points = 16

# Pontos e pesos de Gauss-Legendre
x, w = np.polynomial.legendre.leggauss(n_points)

# Transformação dos pontos e pesos para o intervalo [a, b]
x_mapped = 0.5 * (b - a) * x + 0.5 * (b + a)
w_mapped = 0.5 * (b - a) * w

# Cálculo da integral usando a regra de quadratura de Gauss-Legendre
integral_value = np.sum(w_mapped * integrand(x_mapped))

# Exibição do resultado com três casas decimais
print("Valor da integral:", round(integral_value, 3))
