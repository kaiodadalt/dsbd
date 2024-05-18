# Dados
xi <- c(2, 2, 1, 6, 3, 1, 1, 1, 0, 0)
yi <- c(-0.494, 1.752, -0.444, 2.331, 0.310, -0.030, -1.452, 0.658, -0.415, -1.806)

# Função de perda
loss_function <- function(beta) {
  mu <- beta[1] + beta[2] * xi
  loss <- sum(abs(yi - mu))
  return(loss)
}

# Otimização usando Nelder-Mead
result <- optim(c(0, 0), loss_function)

# Resultados
beta0 <- result$par[1]
beta1 <- result$par[2]
loss <- result$value

# Imprimir resultados
cat("Valor de beta0:", round(beta0, 3), "\n")
cat("Valor de beta1:", round(beta1, 3), "\n")
cat("Valor da função objetivo no ponto ótimo:", round(loss, 3), "\n")
