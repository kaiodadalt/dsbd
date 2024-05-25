# Dados
y <- c(4, 6, 5, 7, 7, 2, 5, 7, 5, 5)
n <- length(y)
m <- mean(y)

# Função objetivo
f <- function(mu) {
  sum_val <- 0
  for (i in 1:n) {
    sum_val <- sum_val + 2 * (y[i] * log(y[i] / (mu * m)) / mu + (m - y[i]) * log((1 - y[i] / mu) / (1 - mu)))
  }
  sum_val - 3.84
}

# Gradiente da função objetivo
grad_f <- function(mu) {
  gradient <- 0
  for (i in 1:n) {
    gradient <- gradient + (-2 * y[i] / (mu^2) + 2 * (y[i] - m) / ((1 - mu)^2)) / (y[i] / (mu * m) + (m - y[i]) / (1 - mu))
  }
  gradient
}

# Método do gradiente descendente
grad_desc <- function(f, grad_f, mu_init, learning_rate, epsilon) {
  mu_current <- mu_init
  iter <- 0
  while (TRUE) {
    iter <- iter + 1
    mu_new <- mu_current - learning_rate * grad_f(mu_current)
    if (abs(mu_new - mu_current) < epsilon) {
      break
    }
    mu_current <- mu_new
  }
  return(mu_current)
}

# Parâmetros
mu_init <- 0.5  # Valor inicial
learning_rate <- 0.01  # Taxa de aprendizado
epsilon <- 0.0001  # Tolerância

# Execução do gradiente descendente
raiz <- grad_desc(f, grad_f, mu_init, learning_rate, epsilon)

# Exibição do resultado com três casas decimais
cat("Valor da raiz:", round(raiz, 3), "\n")

