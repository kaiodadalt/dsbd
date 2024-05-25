import numpy as np

# Definir as funções correspondentes às equações do sistema
def f1(x, y):
    return np.sin(x*y) + np.exp(y) - 7.10964

def f2(x, y):
    return (x + y)**2 - np.cos(x*y**2) - 24.1561

# Calcular as derivadas parciais das funções em relação a x e y
def df1_dx(x, y):
    return y * np.cos(x*y)

def df1_dy(x, y):
    return x * np.cos(x*y) + np.exp(y)

def df2_dx(x, y):
    return 2*(x + y) + y**2 * np.sin(x*y**2)

def df2_dy(x, y):
    return 2*(x + y) - 2*y * np.sin(x*y**2) * np.sin(x*y**2)

# Implementar o método de Newton
def newton_system(f1, f2, df1_dx, df1_dy, df2_dx, df2_dy, x0, y0, epsilon=0.0001, max_iter=100):
    for i in range(max_iter):
        F = np.array([f1(x0, y0), f2(x0, y0)])
        J = np.array([[df1_dx(x0, y0), df1_dy(x0, y0)],
                      [df2_dx(x0, y0), df2_dy(x0, y0)]])
        delta = np.linalg.solve(J, -F)
        x0 += delta[0]
        y0 += delta[1]
        if np.linalg.norm(delta) < epsilon:
            return x0, y0
    print("O método de Newton não convergiu.")
    return None, None

# Escolher valores iniciais adequados
x0, y0 = 1, 1

# Resolver o sistema
x_hat, y_hat = newton_system(f1, f2, df1_dx, df1_dy, df2_dx, df2_dy, x0, y0)

# Exibir as raízes encontradas
print("As raízes do sistema são:")
print("x̂ =", round(x_hat, 3))
print("ŷ =", round(y_hat, 3))
