# Definindo a função a ser integrada
f <- function(x, kappa) {
  return(1 / (kappa + 1/kappa) * exp(-x / kappa))
}

# Definindo o número de pontos de integração
n <- 1088

# Fixando a semente para reproducibilidade
set.seed(123)

# Definindo o valor de kappa
kappa <- 0.5

# Gerando os pontos de amostragem
x <- runif(n, min = -100, max = 100)  # Gerando números aleatórios uniformemente distribuídos

# Calculando a média dos valores da função nos pontos de amostragem
integral <- mean(f(x, kappa))

# Multiplicando pela largura do intervalo
integral <- integral * 200  # (max - min) = 100 - (-100) = 200

print(integral)
