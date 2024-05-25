# Fixar a semente
set.seed(123)

# Definir o número de pontos de integração
n <- 1004

# Definir o valor de mu
mu <- 0.023

# Gerar pontos de integração seguindo uma distribuição normal centrada em mu
x <- rnorm(n, mean = mu)

# Avaliar a função integranda em cada ponto
integrand <- 0.5 * exp(-abs(x - mu))

# Calcular a estimativa da integral
integral_estimate <- mean(integrand)

# Imprimir o resultado
print(paste("Estimativa da integral:", integral_estimate))
