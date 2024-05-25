# Defina os limites de integração
a <- 1.1
b <- 8.1

# Defina os parâmetros
alpha <- 2
beta <- 1

# Defina a função a ser integrada
f <- function(y) {
  (beta^alpha * y^(alpha - 1) * exp(-beta * y)) / gamma(alpha)
}

# Use a função integrate para calcular a integral numericamente
resultado_integral <- integrate(f, lower = a, upper = b)$value

# Exiba o resultado com três casas decimais
print(round(resultado_integral, 3))

