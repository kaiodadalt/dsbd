# Dados
xi <- c(4, 0, 2, 3, 3, 2, 0, 3, 2, 3)
yi <- c(0.046, -1.458, 0.936, -0.637, 0.767, 0.428, -0.945, 2.322, -1.022, 1.106)
n <- length(xi)

# Função objetivo
L <- function(beta) {
  mu <- beta[1] + beta[2] * xi
  sum((yi - mu)^2)
}

# Otimização
result <- optim(c(0, 0), L, method = "Nelder-Mead")

# Resultados
beta0 <- result$par[1]
beta1 <- result$par[2]
valor_objetivo <- result$value

# Exibição dos resultados com três casas decimais
cat("Valor de beta0:", round(beta0, 3), "\n")
cat("Valor de beta1:", round(beta1, 3), "\n")
cat("Valor da função objetivo no ponto ótimo:", round(valor_objetivo, 3), "\n")

