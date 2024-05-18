import numpy as np

# Define as funções do sistema de equações
def equations(vars):
    x, y = vars
    eq1 = x*y + y**2 - 1
    eq2 = x*y**3 + x**2*y**2 + 1
    return [eq1, eq2]

# Define as derivadas parciais das funções em relação a x e y
def jacobian(vars):
    x, y = vars
    return [[y, x + 2*y], [y**3 + 2*x*y**2, 3*x*y**2 + 2*x**2*y]]

# Implementação do método de Newton
def newton_method(equations, jacobian, initial_guess, tolerance=1e-4, max_iterations=100):
    vars = initial_guess
    for i in range(max_iterations):
        fx = np.array(equations(vars))
        J = np.array(jacobian(vars))
        delta = np.linalg.solve(J, -fx)
        vars += delta
        if np.linalg.norm(delta) < tolerance:
            return vars
    raise ValueError("O método de Newton não convergiu.")

# Chute inicial
initial_guess = [1.0, 1.0]

# Tolerância
tolerance = 1e-4

# Encontrar as raízes
root = newton_method(equations, jacobian, initial_guess, tolerance)

# Exibir as raízes
print("Raízes encontradas:")
print("x_hat =", round(root[0], 3))
print("y_hat =", round(root[1], 3))
