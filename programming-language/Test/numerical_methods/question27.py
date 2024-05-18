import numpy as np


# Função f(mu, y)
def f(mu, y):
    return np.sum(2 * (np.exp(mu) * (mu - 1 - y) + np.exp(mu)))


# Derivada da função f em relação a mu
def df(mu, y):
    return np.sum(2 * (np.exp(mu) * (mu - y)))


# Método de Newton para encontrar a raiz
def newton_method(f, df, y, x0, epsilon=0.0001, max_iter=1000):
    xi = x0
    for iteration in range(max_iter):
        f_xi = f(xi, y)
        df_xi = df(xi, y)

        if abs(df_xi) < epsilon:
            print("Derivada próxima de zero. Possível ponto estacionário encontrado.")
            return xi

        xi_plus_1 = xi - f_xi / df_xi
        if abs(xi_plus_1 - xi) < epsilon:
            print("Convergência alcançada após", iteration, "iterações.")
            return xi_plus_1

        xi = xi_plus_1

    print("Número máximo de iterações atingido.")
    return xi


# Valores de y
y = np.array([3.390, 7.379, 1.630, 4.778, 8.874, 5.531, 2.216, 1.582, 7.471, 5.296])

# Valor inicial para o método de Newton
x0 = 1  # Vamos tentar um valor inicial diferente

# Encontrar a raiz usando o método de Newton
raiz = newton_method(f, df, y, x0)

print("Raiz encontrada:", round(raiz, 3))
