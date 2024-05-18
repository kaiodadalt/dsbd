# Fixando a semente
set.seed(123)

# Número de pontos de integração
n <- 1010

# Valor de mu
mu <- -0.019

# Função para avaliar o integrando
f <- function(x) 0.5 * exp(-abs(x - mu))

# Gerando amostras aleatórias de acordo com uma distribuição normal
x_samples <- rnorm(n)

# Avaliando a função nos pontos amostrados
y_samples <- f(x_samples)

# Calculando a média dos valores da função multiplicada pela largura total do intervalo
integral_estimate <- mean(y_samples) * (2 * sd(x_samples))

integral_estimate
