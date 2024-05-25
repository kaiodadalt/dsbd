import numpy as np

# Fixando a semente
np.random.seed(123)

# Parâmetros
kappa = 0.5
n_points = 1088

# Gerando amostras aleatórias de x a partir de uma distribuição exponencial
x_samples = np.random.exponential(scale=kappa, size=n_points)

# Avaliando a função no conjunto de amostras
integrand = 1 / (kappa + 1/kappa) * np.exp(-x_samples / kappa)

# Estimando a integral usando a média das amostras multiplicada pela largura do intervalo
integral_estimate = np.mean(integrand) * kappa * 2

# Exibindo o resultado
print("Estimativa da integral usando Monte Carlo:", integral_estimate)
