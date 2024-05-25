# Definir os dados
xi <- c(2, 2, 2, 0, 0, 1, 3, 1, 2, 2)
yi <- c(1, 0, 1, 0, 0, 0, 0, 0, 1, 0)
n <- length(xi)

# Definir a função de verossimilhança negativa
likelihood <- function(params) {
  beta0 <- params[1]
  beta1 <- params[2]
  mu <- exp(beta0 + beta1 * xi) / (1 + exp(beta0 + beta1 * xi))
  L <- -mean(yi * log(mu) + (1 - yi) * log(1 - mu))
  return(L)
}

# Encontrar os valores ótimos de beta0 e beta1
result <- optim(c(0, 0), likelihood)
beta0_opt <- result$par[1]
beta1_opt <- result$par[2]
L_opt <- result$value

# Mostrar os resultados
cat("Valor de beta0:", round(beta0_opt, 3), "\n")
cat("Valor de beta1:", round(beta1_opt, 3), "\n")
cat("Valor da função objetivo no ponto ótimo:", round(L_opt, 3), "\n")
