# Definir os dados
xi <- c(3, 3, 1, 0, 3, 1, 1, 1, 1, 2)
yi <- c(-1.775, -0.426, -2.000, -1.446, 0.850, -0.308, -0.284, -0.299, 0.264, 0.337)
n <- length(xi)

# Função objetivo
L <- function(beta) {
  mu <- beta[1] + beta[2] * xi
  sum(log(cosh(mu - yi)))
}

# Valor inicial
beta_init <- c(0, 0)

# Otimização usando SANN
result <- optim(beta_init, L, method = "SANN")

# Extrair os valores ótimos de beta0, beta1 e a função objetivo no ponto ótimo
beta0_opt <- result$par[1]
beta1_opt <- result$par[2]
obj_value <- result$value

# Imprimir os resultados
cat("Valor ótimo de beta0:", round(beta0_opt, 3), "\n")
cat("Valor ótimo de beta1:", round(beta1_opt, 3), "\n")
cat("Valor da função objetivo no ponto ótimo:", round(obj_value, 3), "\n")
