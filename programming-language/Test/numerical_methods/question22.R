# Dados
xi <- c(2, 1, 5, 2, 1, 1, 0, 1, 0, 2)
yi <- c(-1.189, -0.364, -1.313, 2.018, 0.489, -1.458, -1.498, 0.267, -1.034, 1.950)
n <- length(xi)

# Função objetivo
objective_function <- function(beta){
  mu <- beta[1] + beta[2]*xi
  sum_abs_diff <- sum(abs(yi - mu))
  return(sum_abs_diff)
}

# Valores iniciais
initial_values <- c(0, 0)

# Otimização usando Simulated Annealing
optim_result <- optim(par = initial_values, fn = objective_function, method = "SANN")

# Resultados
beta0_opt <- optim_result$par[1]
beta1_opt <- optim_result$par[2]
objective_value <- optim_result$value

# Exibindo os resultados
print(paste("Valor de beta0:", round(beta0_opt, 3)))
print(paste("Valor de beta1:", round(beta1_opt, 3)))
print(paste("Valor da função objetivo no ponto ótimo:", round(objective_value, 3)))

